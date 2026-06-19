# Daftar dokumen yang didukung beserta section-nya

DOCUMENT_TYPES = {
    "Proposal Penelitian": [
        "Judul", "Latar Belakang", "Rumusan Masalah", "Tujuan Penelitian",
        "Manfaat Penelitian", "Tinjauan Pustaka", "Kerangka Teori",
        "Hipotesis", "Metodologi Penelitian", "Jadwal Penelitian", "Daftar Pustaka",
    ],
    "Proposal Skripsi": [
        "Judul", "Latar Belakang", "Rumusan Masalah", "Tujuan Penelitian",
        "Manfaat Penelitian", "Tinjauan Pustaka", "Kerangka Teori",
        "Metodologi Penelitian", "Daftar Pustaka",
    ],
    "Skripsi": [
        "Abstrak", "BAB I Pendahuluan", "BAB II Tinjauan Pustaka",
        "BAB III Metodologi Penelitian", "BAB IV Hasil dan Pembahasan",
        "BAB V Kesimpulan dan Saran", "Daftar Pustaka",
    ],
    "Tesis": [
        "Abstrak", "BAB I Pendahuluan", "BAB II Tinjauan Pustaka",
        "BAB III Metodologi Penelitian", "BAB IV Hasil dan Pembahasan",
        "BAB V Kesimpulan dan Saran", "Daftar Pustaka",
    ],
    "Makalah": [
        "Judul", "Pendahuluan", "Pembahasan", "Penutup", "Daftar Pustaka",
    ],
    "Laporan Penelitian": [
        "Judul", "Executive Summary", "Pendahuluan", "Tinjauan Pustaka",
        "Metodologi", "Hasil Penelitian", "Pembahasan",
        "Kesimpulan dan Saran", "Daftar Pustaka",
    ],
    "Manuskrip Jurnal Ilmiah": [
        "Judul", "Abstract", "Pendahuluan", "Tinjauan Pustaka",
        "Metodologi", "Hasil dan Pembahasan", "Kesimpulan", "Daftar Pustaka",
    ],
}

CITATION_STYLES = ["APA", "MLA", "Chicago", "Vancouver", "IEEE"]
LANGUAGES       = ["Indonesian", "English"]

# Alias input user → nama resmi
DOC_TYPE_ALIASES = {
    "skripsi": "Skripsi",
    "tesis": "Tesis",
    "makalah": "Makalah",
    "proposal": "Proposal Penelitian",
    "proposal penelitian": "Proposal Penelitian",
    "proposal skripsi": "Proposal Skripsi",
    "laporan": "Laporan Penelitian",
    "laporan penelitian": "Laporan Penelitian",
    "jurnal": "Manuskrip Jurnal Ilmiah",
    "manuskrip": "Manuskrip Jurnal Ilmiah",
    "artikel jurnal": "Manuskrip Jurnal Ilmiah",
    "thesis": "Tesis",
    "paper": "Makalah",
    "report": "Laporan Penelitian",
}

CITATION_ALIASES = {
    "apa": "APA", "mla": "MLA", "chicago": "Chicago",
    "vancouver": "Vancouver", "ieee": "IEEE",
}

LANGUAGE_ALIASES = {
    "indonesia": "Indonesian", "indonesian": "Indonesian",
    "inggris": "English", "english": "English",
    "indo": "Indonesian", "eng": "English",
}


def resolve_doc_type(raw: str) -> str | None:
    return DOC_TYPE_ALIASES.get(raw.strip().lower())


def resolve_citation(raw: str) -> str | None:
    return CITATION_ALIASES.get(raw.strip().lower())


def resolve_language(raw: str) -> str | None:
    return LANGUAGE_ALIASES.get(raw.strip().lower())
