# CleverDoc CLI Agent

CLI chatbot untuk generate dokumen akademik secara otomatis melalui percakapan natural.

Dibangun di atas ekosistem [CleverDoc](https://cleverdoc.id) dengan memanfaatkan DeepSeek LLM untuk ekstraksi intent dan generasi konten dokumen.

---

## Fitur

- Percakapan natural — cukup ketik kebutuhan Anda, agent akan memandu
- Deteksi parameter otomatis dari satu kalimat (jenis dokumen, topik, bahasa, gaya sitasi)
- Generate dokumen lengkap section per section dengan progress bar
- Output berupa file `.docx` siap pakai
- Mendukung 7 jenis dokumen akademik

## Jenis Dokumen yang Didukung

| Dokumen | Jumlah Section |
|---|---|
| Proposal Penelitian | 11 |
| Proposal Skripsi | 9 |
| Skripsi | 7 |
| Tesis | 7 |
| Makalah | 5 |
| Laporan Penelitian | 9 |
| Manuskrip Jurnal Ilmiah | 8 |

Gaya sitasi: **APA, MLA, Chicago, Vancouver, IEEE**  
Bahasa: **Indonesian, English**

---

## Instalasi

**Prasyarat:** Python 3.10+

```bash
# Clone repository
git clone https://github.com/laode2010/generate_document_cli_agent.git
cd generate_document_cli_agent

# (Opsional) Buat virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux

# Install dependencies
pip install -r requirements.txt
```

## Konfigurasi

```bash
# Salin template konfigurasi
copy .env.example .env    # Windows
# cp .env.example .env    # Mac/Linux
```

Edit `.env` dan isi API key Anda:

```env
DEEPSEEK_API_KEY=sk-...
DEEPSEEK_MODEL=deepseek-chat

GEMINI_API_KEY=AIza...      # opsional
GEMINI_MODEL=gemini-2.5-flash

CONTENT_PROVIDER=deepseek   # deepseek atau gemini
OUTPUT_DIR=output
```

> API key DeepSeek bisa diperoleh di [platform.deepseek.com](https://platform.deepseek.com)

---

## Penggunaan

```bash
python agent.py
```

**Contoh sesi:**

```
🤖 CleverDoc: Dokumen apa yang ingin Anda buat?

👤 Anda: buatkan skripsi tentang pengaruh AI terhadap pendidikan, bahasa Indonesia, APA

🤖 CleverDoc: Berikut ringkasan dokumen yang akan dibuat:
  Jenis dokumen : Skripsi
  Topik         : pengaruh AI terhadap pendidikan
  Bahasa        : Indonesian
  Gaya sitasi   : APA

  Konfirmasi dan mulai generate? (ya/tidak)

👤 Anda: ya

  [████████████████████] 100%  Generating: Daftar Pustaka

🤖 CleverDoc: Dokumen berhasil dibuat!
  📄 File : output/Skripsi_pengaruh_AI_terhadap_pendidikan.docx
```

---

## Struktur Proyek

```
cli_agent/
├── agent.py                  # Entry point CLI
├── config.py                 # Load konfigurasi dari .env
├── requirements.txt
├── .env.example              # Template konfigurasi
└── services/
    ├── conversation.py       # State machine + intent extraction (DeepSeek)
    ├── generator.py          # Generate konten section per section → .docx
    ├── document_types.py     # Daftar dokumen, section, alias resolving
    └── prompts.py            # Template prompt per section
```

## Arsitektur

```
User input
    │
    ▼
ConversationManager          ← DeepSeek (intent extraction, temperature=0.1)
    │  state machine mengumpulkan:
    │  doc_type, topic, language, citation_style
    │
    ▼ (semua parameter lengkap + user konfirmasi)
generate_document()          ← DeepSeek (content generation, temperature=0.7)
    │  generate tiap section secara async
    │
    ▼
_build_docx()                ← python-docx
    │
    ▼
output/<filename>.docx
```

---

## Kontribusi

Pull request terbuka untuk:
- Menambah jenis dokumen baru
- Dukungan provider LLM lain (Gemini, OpenAI, Anthropic)
- Fitur streaming output per section

## Lisensi

MIT License
