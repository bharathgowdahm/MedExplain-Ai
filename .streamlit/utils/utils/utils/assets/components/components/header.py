"""Top header with brand + theme toggle + disclaimer."""
from __future__ import annotations
import streamlit as st

def render_header() -> None:
    with open("assets/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    c1, c2 = st.columns([4, 1])
    with c1:
        st.markdown("### 🩺 MedExplain AI")
        st.caption("Understand Your Health. In Your Language.")
    with c2:
        mode = st.session_state.get("theme_mode", "light")
        if st.button("🌙 Dark" if mode == "light" else "☀️ Light", key="theme_toggle"):
            st.session_state["theme_mode"] = "dark" if mode == "light" else "light"
            st.rerun()
