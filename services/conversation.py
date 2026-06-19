"""
conversation.py — State machine percakapan berbasis DeepSeek.
Mengumpulkan parameter dokumen secara conversational, lalu trigger generate.
"""

import json
import re
from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

from openai import OpenAI

from config import DEEPSEEK_API_KEY, DEEPSEEK_MODEL
from services.document_types import (
    DOCUMENT_TYPES, CITATION_STYLES, LANGUAGES,
    resolve_doc_type, resolve_citation, resolve_language,
)


# ── State percakapan ────────────────────────────────────────────────────────

class State(str, Enum):
    GREETING      = "greeting"
    COLLECT_TYPE  = "collect_type"
    COLLECT_TOPIC = "collect_topic"
    COLLECT_LANG  = "collect_lang"
    COLLECT_CITE  = "collect_cite"
    CONFIRM       = "confirm"
    GENERATING    = "generating"
    DONE          = "done"


@dataclass
class Session:
    state: State = State.GREETING
    doc_type: Optional[str]       = None
    topic: Optional[str]          = None
    language: Optional[str]       = None
    citation_style: Optional[str] = None
    history: list                 = field(default_factory=list)

    @property
    def is_complete(self) -> bool:
        return all([self.doc_type, self.topic, self.language, self.citation_style])

    def summary(self) -> str:
        return (
            f"  Jenis dokumen : {self.doc_type}\n"
            f"  Topik         : {self.topic}\n"
            f"  Bahasa        : {self.language}\n"
            f"  Gaya sitasi   : {self.citation_style}"
        )


# ── Intent extraction via DeepSeek ─────────────────────────────────────────

INTENT_SYSTEM = """
Kamu adalah ekstraktor intent untuk chatbot generator dokumen akademik.
Dari pesan user, ekstrak parameter berikut jika disebutkan.

Dokumen yang dikenali (gunakan nama persis ini):
- Proposal Penelitian
- Proposal Skripsi
- Skripsi
- Tesis
- Makalah
- Laporan Penelitian
- Manuskrip Jurnal Ilmiah

Gaya sitasi yang dikenali: APA, MLA, Chicago, Vancouver, IEEE
Bahasa yang dikenali: Indonesian, English

Kembalikan HANYA JSON (tanpa markdown, tanpa penjelasan):
{
  "doc_type": null,
  "topic": null,
  "language": null,
  "citation_style": null,
  "is_confirmation": false,
  "is_cancellation": false
}

Isi nilai dengan string jika disebutkan, tetap null jika tidak disebutkan.
is_confirmation=true jika user menyatakan setuju/konfirmasi/lanjut.
is_cancellation=true jika user ingin batal/cancel.
"""


def _extract_intent(client: OpenAI, user_msg: str, context: str) -> dict:
    """Panggil DeepSeek untuk ekstrak parameter dari pesan user."""
    try:
        resp = client.chat.completions.create(
            model=DEEPSEEK_MODEL,
            messages=[
                {"role": "system", "content": INTENT_SYSTEM},
                {"role": "user", "content": f"Konteks: {context}\n\nPesan user: {user_msg}"},
            ],
            max_tokens=200,
            temperature=0.1,  # deterministic untuk parsing
        )
        raw = resp.choices[0].message.content.strip()
        raw = re.sub(r"```json|```", "", raw).strip()
        return json.loads(raw)
    except json.JSONDecodeError:
        return {}
    except Exception:
        return {}


def _resolve_extracted(extracted: dict) -> dict:
    """Normalize nilai yang diekstrak ke nilai resmi."""
    result = {}

    doc_type = extracted.get("doc_type")
    if doc_type:
        resolved = resolve_doc_type(doc_type.lower())
        if resolved:
            result["doc_type"] = resolved
        elif doc_type in DOCUMENT_TYPES:
            result["doc_type"] = doc_type

    topic = extracted.get("topic")
    if topic and len(topic.strip()) > 2:
        result["topic"] = topic.strip()

    language = extracted.get("language")
    if language:
        resolved = resolve_language(language.lower())
        if resolved:
            result["language"] = resolved

    citation = extracted.get("citation_style")
    if citation:
        resolved = resolve_citation(citation.lower())
        if resolved:
            result["citation_style"] = resolved
        elif citation.upper() in CITATION_STYLES:
            result["citation_style"] = citation.upper()

    return result


# ── Conversation Manager ────────────────────────────────────────────────────

class ConversationManager:

    NEXT_QUESTION = {
        "doc_type": (
            "Dokumen apa yang ingin Anda buat?\n"
            "  Pilihan: Proposal Penelitian, Proposal Skripsi, Skripsi, Tesis,\n"
            "           Makalah, Laporan Penelitian, Manuskrip Jurnal Ilmiah"
        ),
        "topic": "Apa topik {doc_type} Anda?",
        "language": "Dalam bahasa apa dokumen dibuat? (Indonesian / English)",
        "citation_style": "Gaya sitasi apa yang digunakan? (APA / MLA / Chicago / Vancouver / IEEE)",
    }

    def __init__(self):
        if not DEEPSEEK_API_KEY:
            raise RuntimeError("DEEPSEEK_API_KEY belum diset di .env")
        self._client = OpenAI(
            api_key=DEEPSEEK_API_KEY,
            base_url="https://api.deepseek.com",
        )

    def _missing_params(self, session: Session) -> list[str]:
        order = ["doc_type", "topic", "language", "citation_style"]
        return [p for p in order if not getattr(session, p)]

    def process(self, session: Session, user_msg: str) -> tuple[str, bool]:
        """
        Proses pesan user, update session.
        Returns (reply_text, should_generate).
        should_generate=True → semua param terkumpul dan user konfirmasi.
        """
        context = (
            f"state={session.state}, doc_type={session.doc_type}, "
            f"topic={session.topic}, language={session.language}, "
            f"citation_style={session.citation_style}"
        )

        extracted = _extract_intent(self._client, user_msg, context)
        resolved  = _resolve_extracted(extracted)

        # Update session dengan parameter yang berhasil diekstrak
        for key, value in resolved.items():
            setattr(session, key, value)

        # Cek pembatalan
        if extracted.get("is_cancellation"):
            session.state = State.GREETING
            session.doc_type = session.topic = session.language = session.citation_style = None
            return "Baik, sesi dibatalkan. Ketik 'mulai' jika ingin membuat dokumen baru.", False

        # Jika semua parameter sudah terkumpul
        if session.is_complete:
            if session.state == State.CONFIRM:
                # Cek konfirmasi user
                confirmed = extracted.get("is_confirmation") or any(
                    w in user_msg.lower()
                    for w in ["ya", "yes", "iya", "ok", "lanjut", "generate", "buat", "mulai"]
                )
                if confirmed:
                    session.state = State.GENERATING
                    return "", True
                else:
                    return self._ask_change(session), False
            else:
                session.state = State.CONFIRM
                return self._confirmation_message(session), False

        # Masih ada parameter kurang → tanya berikutnya
        missing = self._missing_params(session)
        next_param = missing[0]
        question = self.NEXT_QUESTION[next_param].format(
            doc_type=session.doc_type or "dokumen"
        )

        if session.state == State.GREETING:
            session.state = State.COLLECT_TYPE

        return question, False

    def _confirmation_message(self, session: Session) -> str:
        return (
            "Berikut ringkasan dokumen yang akan dibuat:\n\n"
            f"{session.summary()}\n\n"
            "Konfirmasi dan mulai generate? (ya/tidak)"
        )

    def _ask_change(self, session: Session) -> str:
        return (
            "Apa yang ingin diubah? Contoh:\n"
            "  'topiknya tentang blockchain'\n"
            "  'ganti ke APA style'\n"
            "  'pakai bahasa Inggris'\n\n"
            f"Parameter saat ini:\n{session.summary()}"
        )
