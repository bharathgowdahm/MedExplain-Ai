"""Elegant sidebar navigation with icons and active states."""
from __future__ import annotations
import streamlit as st
from components.language_selector import language_selector

NAV = [
    ("🏠", "Home Dashboard", "pages/1_Home.py"),
    ("📤", "Upload & Analyze", "pages/2_Upload_Analyze.py"),
    ("📋", "My Report Explanation", "pages/3_Report_Explanation.py"),
    ("💬", "AI Medical Assistant", "pages/4_AI_Assistant.py"),
    ("📈", "Health Trends", "pages/5_Health_Trends.py"),
    ("📖", "Medical Dictionary", "pages/6_Medical_Dictionary.py"),
    ("🩺", "Doctor Visit Preparation", "pages/7_Doctor_Preparation.py"),
    ("🗂️", "Report History", "pages/8_Report_History.py"),
    ("🔒", "Privacy & Settings", "pages/9_Privacy_Settings.py"),
    ("❓", "Help & About", "pages/10_Help.py"),
]

def render_sidebar() -> None:
    st.sidebar.title("🩺 MedExplain AI")
    st.sidebar.caption("Educational health explanations")
    language_selector("sidebar")
    st.sidebar.divider()
    for icon, label, path in NAV:
        # st.page_link gives active state automatically
        try:
            st.sidebar.page_link(path, label=f"{icon} {label}")
        except Exception:
            st.sidebar.markdown(f"{icon} {label}")
    st.sidebar.divider()
    st.sidebar.info(
        "🔒 Privacy-first: reports stay in your session unless you explicitly save them."
    )
