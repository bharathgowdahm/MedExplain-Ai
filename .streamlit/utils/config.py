"""Central configuration. Secrets only from env / Streamlit secrets."""
from __future__ import annotations
import os

BRAND = {
    "primary_navy": "#102A43",
    "medical_teal": "#00A896",
    "emerald": "#10B981",
    "background": "#F7FAFC",
    "surface": "#FFFFFF",
    "muted_text": "#64748B",
    "warning": "#F59E0B",
    "error": "#DC2626",
}

LANGUAGES = {
    "en": "English",
    "kn": "ಕನ್ನಡ",
    "hi": "हिन्दी",
}

DISCLAIMER_EN = (
    "MedExplain AI provides educational explanations only. "
    "It does not diagnose medical conditions or replace professional medical advice."
)

def get_secret(name: str, default: str = "") -> str:
    # 1) Streamlit secrets (lazy import so plain python also works)
    try:
        import streamlit as st
        if hasattr(st, "secrets") and name in st.secrets:
            return str(st.secrets[name])
    except Exception:
        pass
    # 2) Environment variable
    return os.getenv(name, default)

APP_ENV: str = get_secret("APP_ENV", "development")
GEMINI_API_KEY: str = get_secret("GEMINI_API_KEY", "")
GEMINI_MODEL: str = get_secret("GEMINI_MODEL", "gemini-2.0-flash")
MAX_UPLOAD_MB: int = 10
