"""Safe session-state defaults. No report content cached across users."""
from __future__ import annotations
import streamlit as st

DEFAULTS = {
    "language": "en",            # en | kn | hi
    "theme_mode": "light",       # light | dark
    "private_session": True,     # privacy-by-default
    "persist_reports": False,    # explicit opt-in only
    "consent_ai_processing": False,
    "current_report": None,      # dict with extracted measurements
    "report_history": [],        # list of saved summaries (explicit save only)
    "chat_history": [],          # per-session chat
    "plain_language_level": 1,   # 0 simple | 1 standard | 2 detailed | 3 ELI12
    "bilingual_view": False,
}

def init_session() -> None:
    for k, v in DEFAULTS.items():
        if k not in st.session_state:
            st.session_state[k] = v

def clear_session_data() -> None:
    """Delete all session health data (privacy requirement)."""
    for k in ["current_report", "report_history", "chat_history"]:
        st.session_state[k] = [] if k != "current_report" else None
    st.session_state["consent_ai_processing"] = False

def set_language(code: str) -> None:
    if code in ("en", "kn", "hi"):
        st.session_state["language"] = code
