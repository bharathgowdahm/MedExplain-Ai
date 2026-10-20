"""Language selector component (English / Kannada / Hindi)."""
from __future__ import annotations
import streamlit as st
from utils.config import LANGUAGES
from utils.session_manager import set_language

def language_selector(location: str = "sidebar") -> str:
    current = st.session_state.get("language", "en")
    labels = [f"{LANGUAGES[c]}" for c in ["en", "kn", "hi"]]
    codes = ["en", "kn", "hi"]
    idx = codes.index(current)
    key = f"lang_select_{location}"
    if location == "sidebar":
        sel = st.sidebar.radio("Language / ಭಾಷೆ / भाषा", labels, index=idx, key=key)
    else:
        sel = st.radio("Language / ಭಾಷೆ / भाषा", labels, index=idx, key=key, horizontal=True)
    set_language(codes[labels.index(sel)])
    return st.session_state["language"]
