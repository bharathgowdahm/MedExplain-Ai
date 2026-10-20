"""MedExplain AI — main entry. Streamlit multipage app."""
from __future__ import annotations
import streamlit as st
from utils.session_manager import init_session
from components.sidebar import render_sidebar
from components.header import render_header

st.set_page_config(
    page_title="MedExplain AI — Understand Your Health",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)

init_session()
render_header()
render_sidebar()

st.switch_page("pages/1_Home.py")
