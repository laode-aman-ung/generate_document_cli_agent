#!/usr/bin/env python3
"""
CleverDoc CLI Agent
Chatbot conversational untuk generate dokumen akademik.

Usage:
    python agent.py
"""

import asyncio
import sys
import os

# Pastikan import dari folder cli_agent
sys.path.insert(0, os.path.dirname(__file__))

from services.conversation import ConversationManager, Session, State
from services.generator import generate_document

# ── Warna terminal ──────────────────────────────────────────────────────────
RESET  = "\033[0m"
BOLD   = "\033[1m"
CYAN   = "\033[96m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
RED    = "\033[91m"
DIM    = "\033[2m"


def bot(text: str):
    print(f"\n{CYAN}{BOLD}🤖 CleverDoc:{RESET} {text}\n")


def user_prompt() -> str:
    try:
        return input(f"{YELLOW}{BOLD}👤 Anda:{RESET} ").strip()
    except (KeyboardInterrupt, EOFError):
        return "keluar"


def progress_bar(section: str, idx: int, total: int):
    filled = int((idx / total) * 20)
    bar = "█" * filled + "░" * (20 - filled)
    pct = int((idx / total) * 100)
    print(f"\r  [{bar}] {pct:3d}%  Generating: {section[:40]:<40}", end="", flush=True)


def print_header():
    print(f"""
{CYAN}{BOLD}╔══════════════════════════════════════════════════╗
║          CleverDoc Agent  ✦  CLI Edition         ║
║     Generate dokumen akademik via percakapan     ║
╚══════════════════════════════════════════════════╝{RESET}
{DIM}Ketik 'keluar' atau tekan Ctrl+C untuk berhenti.{RESET}
""")


async def run_agent():
    print_header()

    manager = ConversationManager()
    session = Session()

    bot(
        "Halo! Saya CleverDoc Agent.\n"
        "  Saya bisa membantu Anda membuat dokumen akademik seperti skripsi,\n"
        "  tesis, proposal, makalah, laporan, dan jurnal ilmiah.\n\n"
        "  Dokumen apa yang ingin Anda buat?"
    )

    while True:
        user_input = user_prompt()

        if not user_input:
            continue

        if user_input.lower() in ("keluar", "exit", "quit", "q"):
            bot("Sampai jumpa! Semoga sukses dengan dokumen Anda. 👋")
            break

        # Proses pesan via ConversationManager
        reply, should_generate = manager.process(session, user_input)

        if should_generate:
            # ── Mulai generate ──────────────────────────────────────────────
            print(f"\n{GREEN}{BOLD}✅ Parameter lengkap! Memulai generate...{RESET}\n")

            try:
                filepath = await generate_document(
                    doc_type=session.doc_type,
                    topic=session.topic,
                    language=session.language,
                    citation_style=session.citation_style,
                    progress_callback=progress_bar,
                )
                print()  # newline setelah progress bar
                bot(
                    f"{GREEN}Dokumen berhasil dibuat!{RESET}\n\n"
                    f"  📄 File : {BOLD}{filepath}{RESET}\n\n"
                    "  Ingin membuat dokumen lain? (ya/tidak)"
                )
                session.state = State.DONE

            except RuntimeError as e:
                bot(f"{RED}Error: {e}{RESET}")
                break
            except Exception as e:
                bot(f"{RED}Terjadi kesalahan: {e}{RESET}\n  Coba lagi atau ketik 'keluar'.")
                session.state = State.CONFIRM  # balik ke konfirmasi

        elif reply:
            bot(reply)

        # Setelah DONE — tanya apakah mau buat lagi
        if session.state == State.DONE:
            user_input = user_prompt()
            if user_input.lower() in ("ya", "yes", "iya", "y", "lagi"):
                session = Session()  # reset session
                bot(
                    "Baik! Mari buat dokumen baru.\n\n"
                    "  Dokumen apa yang ingin Anda buat?"
                )
            else:
                bot("Terima kasih sudah menggunakan CleverDoc Agent. Sampai jumpa! 👋")
                break


def main():
    try:
        asyncio.run(run_agent())
    except KeyboardInterrupt:
        print(f"\n\n{DIM}Session dihentikan.{RESET}\n")


if __name__ == "__main__":
    main()
