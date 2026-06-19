# Template prompt per section, diadaptasi dari CleverDoc prompt library

SECTION_PROMPTS: dict[str, dict[str, str]] = {

    # ── PROPOSAL PENELITIAN ─────────────────────────────────────────────────
    "Proposal Penelitian": {
        "Judul": """
Anda adalah asisten akademik ahli merumuskan judul penelitian.
Buat judul yang menarik, ringkas, dan menangkap esensi dari:
- Topik: {topic}
- Bahasa: {language}

Judul harus spesifik, terukur, dan sesuai standar akademik.
BUAT JUDUL SEKARANG (hanya judul, tanpa penjelasan):
""",
        "Latar Belakang": """
Anda adalah penulis akademik ahli proposal penelitian.
Tulis bagian "LATAR BELAKANG" untuk:
- Topik: {topic}
- Bahasa: {language}
- Gaya Sitasi: {citation_style}

Wajib: konteks & urgensi, gap literatur, justifikasi penelitian, 3-4 paragraf, bahasa formal.
TULIS LATAR BELAKANG:
""",
        "Rumusan Masalah": """
Tulis "RUMUSAN MASALAH" untuk penelitian tentang:
- Topik: {topic}
- Bahasa: {language}

Buat 3-5 pertanyaan penelitian yang jelas, spesifik, dan dapat diuji.
TULIS RUMUSAN MASALAH:
""",
        "Tujuan Penelitian": """
Tulis "TUJUAN PENELITIAN" berdasarkan:
- Topik: {topic}
- Bahasa: {language}

Buat 3-5 tujuan yang terukur, konsisten dengan rumusan masalah.
TULIS TUJUAN PENELITIAN:
""",
        "Manfaat Penelitian": """
Tulis "MANFAAT PENELITIAN" untuk topik: {topic}
Bahasa: {language}

Bedakan manfaat teoretis dan praktis. Jelaskan kontribusi bagi stakeholder.
TULIS MANFAAT PENELITIAN:
""",
        "Tinjauan Pustaka": """
Tulis "TINJAUAN PUSTAKA" komprehensif untuk:
- Topik: {topic}
- Bahasa: {language}
- Gaya Sitasi: {citation_style}

Cakup: teori utama, penelitian terdahulu yang relevan, posisi penelitian ini.
Sertakan minimal 5 referensi akademik dengan format {citation_style}.
TULIS TINJAUAN PUSTAKA:
""",
        "Kerangka Teori": """
Tulis "KERANGKA TEORI" untuk penelitian tentang: {topic}
Bahasa: {language}

Jelaskan konsep-konsep kunci, hubungan antar variabel, dan model/kerangka konseptual.
TULIS KERANGKA TEORI:
""",
        "Hipotesis": """
Buat "HIPOTESIS" penelitian untuk topik: {topic}
Bahasa: {language}

Rumuskan H0 dan H1 yang testable dan berdasarkan kajian teori.
TULIS HIPOTESIS:
""",
        "Metodologi Penelitian": """
Tulis "METODOLOGI PENELITIAN" untuk:
- Topik: {topic}
- Bahasa: {language}

Cakup: jenis penelitian, populasi & sampel, instrumen, teknik pengumpulan & analisis data.
TULIS METODOLOGI PENELITIAN:
""",
        "Jadwal Penelitian": """
Buat "JADWAL PENELITIAN" dalam bentuk tabel untuk topik: {topic}
Bahasa: {language}

Buat timeline 6 bulan yang realistis mencakup semua tahapan penelitian.
TULIS JADWAL PENELITIAN:
""",
        "Daftar Pustaka": """
Buat "DAFTAR PUSTAKA" untuk penelitian tentang: {topic}
Gaya sitasi: {citation_style}
Bahasa: {language}

Buat minimal 10 referensi akademik yang relevan dan terpercaya.
TULIS DAFTAR PUSTAKA:
""",
    },

    # ── PROPOSAL SKRIPSI ────────────────────────────────────────────────────
    "Proposal Skripsi": {
        "Judul": """
Buat judul skripsi yang tepat dan akademik untuk:
- Topik: {topic}
- Bahasa: {language}
BUAT JUDUL (hanya judul):
""",
        "Latar Belakang": """
Tulis "LATAR BELAKANG" proposal skripsi tentang: {topic}
Bahasa: {language} | Sitasi: {citation_style}

Jelaskan urgensi topik, kesenjangan penelitian, dan relevansi di era sekarang.
TULIS LATAR BELAKANG:
""",
        "Rumusan Masalah": """
Buat "RUMUSAN MASALAH" skripsi untuk topik: {topic}
Bahasa: {language}
TULIS RUMUSAN MASALAH (3-4 pertanyaan):
""",
        "Tujuan Penelitian": """
Buat "TUJUAN PENELITIAN" skripsi untuk topik: {topic}
Bahasa: {language}
TULIS TUJUAN PENELITIAN:
""",
        "Manfaat Penelitian": """
Buat "MANFAAT PENELITIAN" skripsi untuk topik: {topic}
Bahasa: {language}
TULIS MANFAAT (teoretis & praktis):
""",
        "Tinjauan Pustaka": """
Tulis "TINJAUAN PUSTAKA" untuk skripsi tentang: {topic}
Bahasa: {language} | Sitasi: {citation_style}
TULIS TINJAUAN PUSTAKA:
""",
        "Kerangka Teori": """
Tulis "KERANGKA TEORI" untuk skripsi tentang: {topic}
Bahasa: {language}
TULIS KERANGKA TEORI:
""",
        "Metodologi Penelitian": """
Tulis "METODOLOGI PENELITIAN" untuk skripsi tentang: {topic}
Bahasa: {language}
TULIS METODOLOGI:
""",
        "Daftar Pustaka": """
Buat "DAFTAR PUSTAKA" untuk skripsi tentang: {topic}
Sitasi: {citation_style} | Bahasa: {language}
TULIS DAFTAR PUSTAKA (minimal 10 referensi):
""",
    },

    # ── SKRIPSI ─────────────────────────────────────────────────────────────
    "Skripsi": {
        "Abstrak": """
Tulis "ABSTRAK" skripsi tentang: {topic}
Bahasa: {language}

Cakup: latar belakang singkat, tujuan, metode, hasil, kesimpulan. Maks 250 kata.
Sertakan 5 kata kunci.
TULIS ABSTRAK:
""",
        "BAB I Pendahuluan": """
Tulis "BAB I PENDAHULUAN" skripsi tentang: {topic}
Bahasa: {language} | Sitasi: {citation_style}

Sub-bab: 1.1 Latar Belakang, 1.2 Rumusan Masalah, 1.3 Tujuan Penelitian,
1.4 Manfaat Penelitian, 1.5 Batasan Masalah, 1.6 Sistematika Penulisan.
TULIS BAB I:
""",
        "BAB II Tinjauan Pustaka": """
Tulis "BAB II TINJAUAN PUSTAKA" skripsi tentang: {topic}
Bahasa: {language} | Sitasi: {citation_style}

Cakup teori-teori yang relevan, penelitian terdahulu, dan kerangka berpikir.
Sertakan minimal 10 referensi dengan format {citation_style}.
TULIS BAB II:
""",
        "BAB III Metodologi Penelitian": """
Tulis "BAB III METODOLOGI PENELITIAN" untuk skripsi tentang: {topic}
Bahasa: {language}

Sub-bab: 3.1 Jenis Penelitian, 3.2 Tempat & Waktu, 3.3 Populasi & Sampel,
3.4 Instrumen, 3.5 Teknik Pengumpulan Data, 3.6 Teknik Analisis Data.
TULIS BAB III:
""",
        "BAB IV Hasil dan Pembahasan": """
Tulis "BAB IV HASIL DAN PEMBAHASAN" untuk skripsi tentang: {topic}
Bahasa: {language} | Sitasi: {citation_style}

Sajikan hasil analisis data, interpretasi temuan, dan diskusi dengan teori.
Sertakan tabel/angka statistik ilustratif.
TULIS BAB IV:
""",
        "BAB V Kesimpulan dan Saran": """
Tulis "BAB V KESIMPULAN DAN SARAN" untuk skripsi tentang: {topic}
Bahasa: {language}

5.1 Kesimpulan (jawaban langsung dari rumusan masalah)
5.2 Saran (teoritis & praktis)
TULIS BAB V:
""",
        "Daftar Pustaka": """
Buat "DAFTAR PUSTAKA" untuk skripsi tentang: {topic}
Sitasi: {citation_style} | Bahasa: {language}
Minimal 15 referensi akademik terpercaya.
TULIS DAFTAR PUSTAKA:
""",
    },

    # ── TESIS ───────────────────────────────────────────────────────────────
    "Tesis": {
        "Abstrak": """
Tulis "ABSTRAK" tesis (lebih mendalam dari skripsi) tentang: {topic}
Bahasa: {language} | Maks 300 kata.
Cakup: konteks, tujuan, metodologi, temuan utama, implikasi. Sertakan 5-7 kata kunci.
TULIS ABSTRAK:
""",
        "BAB I Pendahuluan": """
Tulis "BAB I PENDAHULUAN" tesis tentang: {topic}
Bahasa: {language} | Sitasi: {citation_style}

Sub-bab: 1.1 Latar Belakang (lebih dalam), 1.2 Identifikasi Masalah,
1.3 Rumusan Masalah, 1.4 Tujuan, 1.5 Manfaat, 1.6 Novelty/Kebaruan Penelitian.
TULIS BAB I:
""",
        "BAB II Tinjauan Pustaka": """
Tulis "BAB II TINJAUAN PUSTAKA" tesis tentang: {topic}
Bahasa: {language} | Sitasi: {citation_style}

Lebih mendalam: cakup grand theory, middle-range theory, penelitian terdahulu terkini,
dan posisi penelitian ini dalam lanskap akademik.
TULIS BAB II:
""",
        "BAB III Metodologi Penelitian": """
Tulis "BAB III METODOLOGI PENELITIAN" tesis tentang: {topic}
Bahasa: {language}

Cakup paradigma penelitian, desain, instrumen, validitas & reliabilitas, etika penelitian.
TULIS BAB III:
""",
        "BAB IV Hasil dan Pembahasan": """
Tulis "BAB IV HASIL DAN PEMBAHASAN" tesis tentang: {topic}
Bahasa: {language} | Sitasi: {citation_style}

Analisis mendalam, triangulasi data, diskusi kritis dengan teori dan implikasi temuan.
TULIS BAB IV:
""",
        "BAB V Kesimpulan dan Saran": """
Tulis "BAB V KESIMPULAN DAN SARAN" tesis tentang: {topic}
Bahasa: {language}

Kesimpulan komprehensif, kontribusi penelitian, keterbatasan, dan agenda penelitian lanjutan.
TULIS BAB V:
""",
        "Daftar Pustaka": """
Buat "DAFTAR PUSTAKA" tesis tentang: {topic}
Sitasi: {citation_style} | Minimal 20 referensi jurnal internasional.
TULIS DAFTAR PUSTAKA:
""",
    },

    # ── MAKALAH ─────────────────────────────────────────────────────────────
    "Makalah": {
        "Judul": "Buat judul makalah akademik untuk topik: {topic}\nBahasa: {language}\nBUAT JUDUL:",
        "Pendahuluan": """
Tulis "PENDAHULUAN" makalah tentang: {topic}
Bahasa: {language} | Sitasi: {citation_style}
Cakup latar belakang, tujuan penulisan, dan sistematika makalah.
TULIS PENDAHULUAN:
""",
        "Pembahasan": """
Tulis "PEMBAHASAN" makalah tentang: {topic}
Bahasa: {language} | Sitasi: {citation_style}
Uraikan secara sistematis dengan sub-judul yang logis. Dukung dengan referensi akademik.
TULIS PEMBAHASAN:
""",
        "Penutup": """
Tulis "PENUTUP" makalah tentang: {topic}
Bahasa: {language}
Cakup kesimpulan dan saran/rekomendasi.
TULIS PENUTUP:
""",
        "Daftar Pustaka": """
Buat "DAFTAR PUSTAKA" makalah tentang: {topic}
Sitasi: {citation_style} | Minimal 8 referensi.
TULIS DAFTAR PUSTAKA:
""",
    },

    # ── LAPORAN PENELITIAN ──────────────────────────────────────────────────
    "Laporan Penelitian": {
        "Judul": "Buat judul laporan penelitian untuk topik: {topic}\nBahasa: {language}\nBUAT JUDUL:",
        "Executive Summary": """
Tulis "EXECUTIVE SUMMARY" laporan penelitian tentang: {topic}
Bahasa: {language}
Ringkasan eksekutif 1 halaman: tujuan, metode, temuan kunci, rekomendasi.
TULIS EXECUTIVE SUMMARY:
""",
        "Pendahuluan": """
Tulis "PENDAHULUAN" laporan penelitian tentang: {topic}
Bahasa: {language} | Sitasi: {citation_style}
TULIS PENDAHULUAN:
""",
        "Tinjauan Pustaka": """
Tulis "TINJAUAN PUSTAKA" laporan penelitian tentang: {topic}
Bahasa: {language} | Sitasi: {citation_style}
TULIS TINJAUAN PUSTAKA:
""",
        "Metodologi": """
Tulis "METODOLOGI" laporan penelitian tentang: {topic}
Bahasa: {language}
TULIS METODOLOGI:
""",
        "Hasil Penelitian": """
Tulis "HASIL PENELITIAN" laporan tentang: {topic}
Bahasa: {language} | Sitasi: {citation_style}
Sajikan data dan temuan secara sistematis.
TULIS HASIL PENELITIAN:
""",
        "Pembahasan": """
Tulis "PEMBAHASAN" laporan penelitian tentang: {topic}
Bahasa: {language} | Sitasi: {citation_style}
TULIS PEMBAHASAN:
""",
        "Kesimpulan dan Saran": """
Tulis "KESIMPULAN DAN SARAN" laporan tentang: {topic}
Bahasa: {language}
TULIS KESIMPULAN DAN SARAN:
""",
        "Daftar Pustaka": """
Buat "DAFTAR PUSTAKA" laporan tentang: {topic}
Sitasi: {citation_style} | Minimal 10 referensi.
TULIS DAFTAR PUSTAKA:
""",
    },

    # ── MANUSKRIP JURNAL ILMIAH ─────────────────────────────────────────────
    "Manuskrip Jurnal Ilmiah": {
        "Judul": "Buat judul artikel jurnal ilmiah untuk topik: {topic}\nBahasa: {language}\nBUAT JUDUL:",
        "Abstract": """
Tulis "ABSTRACT" artikel jurnal tentang: {topic}
Bahasa: {language} | Maks 250 kata.
Struktur: Background, Objective, Methods, Results, Conclusion, Keywords.
TULIS ABSTRACT:
""",
        "Pendahuluan": """
Tulis "PENDAHULUAN" artikel jurnal tentang: {topic}
Bahasa: {language} | Sitasi: {citation_style}
Ikuti struktur IMRaD: konteks, gap, tujuan.
TULIS PENDAHULUAN:
""",
        "Tinjauan Pustaka": """
Tulis "TINJAUAN PUSTAKA" artikel jurnal tentang: {topic}
Bahasa: {language} | Sitasi: {citation_style}
TULIS TINJAUAN PUSTAKA:
""",
        "Metodologi": """
Tulis "METODOLOGI" artikel jurnal tentang: {topic}
Bahasa: {language}
Detail: desain, subjek, instrumen, prosedur, analisis.
TULIS METODOLOGI:
""",
        "Hasil dan Pembahasan": """
Tulis "HASIL DAN PEMBAHASAN" artikel jurnal tentang: {topic}
Bahasa: {language} | Sitasi: {citation_style}
Sajikan hasil lalu interpretasikan dalam konteks literatur yang ada.
TULIS HASIL DAN PEMBAHASAN:
""",
        "Kesimpulan": """
Tulis "KESIMPULAN" artikel jurnal tentang: {topic}
Bahasa: {language}
Ringkas temuan utama dan implikasi praktis/teoretis.
TULIS KESIMPULAN:
""",
        "Daftar Pustaka": """
Buat "DAFTAR PUSTAKA" artikel jurnal tentang: {topic}
Sitasi: {citation_style} | Minimal 15 referensi jurnal internasional.
TULIS DAFTAR PUSTAKA:
""",
    },
}


def get_prompt(doc_type: str, section: str, topic: str, language: str, citation_style: str) -> str:
    """Ambil dan format prompt untuk section tertentu."""
    doc_prompts = SECTION_PROMPTS.get(doc_type, {})
    template = doc_prompts.get(section)
    if not template:
        # Fallback generik
        template = (
            f"Tulis bagian '{section}' untuk {doc_type} tentang: {{topic}}\n"
            f"Bahasa: {{language}} | Sitasi: {{citation_style}}\n"
            f"TULIS {section.upper()}:"
        )
    return template.format(
        topic=topic,
        language=language,
        citation_style=citation_style,
        background_context=topic,
        scope=topic,
    )
