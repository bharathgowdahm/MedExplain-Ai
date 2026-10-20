"""Reusable card components."""
from __future__ import annotations
import streamlit as st

def stat_card(title: str, value: str, subtitle: str = "", tone: str = "ok") -> None:
    st.markdown(
        f"""<div class="med-card"><div class="med-muted" style="font-size:.8rem">{title}</div>
        <div style="font-size:1.6rem;font-weight:800;color:#102A43">{value}</div>
        <span class="med-badge {tone}">{subtitle}</span></div>""",
        unsafe_allow_html=True,
    )

def feature_card(icon: str, title: str, desc: str) -> None:
    st.markdown(
        f"""<div class="med-card"><h4>{icon} {title}</h4>
        <p class="med-muted">{desc}</p></div>""",
        unsafe_allow_html=True,
    )

def disclaimer_box(text: str) -> None:
    st.markdown(f'<div class="med-disclaimer">⚠️ {text}</div>', unsafe_allow_html=True)
