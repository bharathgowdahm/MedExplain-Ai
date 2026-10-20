"""01 Home Dashboard."""
from __future__ import annotations
import streamlit as st
from utils.session_manager import init_session
from utils.config import DISCLAIMER_EN, LANGUAGES
from components.header import render_header
from components.sidebar import render_sidebar
from components.cards import feature_card, disclaimer_box
from components.language_selector import language_selector

st.set_page_config(page_title="Home — MedExplain AI", page_icon="🩺", layout="wide")
init_session()
render_header()
render_sidebar()

lang = st.session_state["language"]

HERO = {
    "en": ("Understand Your Health. In Your Language.",
           "Upload a medical report and understand its terminology, laboratory values, and important questions to discuss with your doctor."),
    "kn": ("ನಿಮ್ಮ ಆರೋಗ್ಯವನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಿ. ನಿಮ್ಮ ಭಾಷೆಯಲ್ಲಿ.",
           "ವೈದ್ಯಕೀಯ ವರದಿಯನ್ನು ಅಪ್‌ಲೋಡ್ ಮಾಡಿ ಮತ್ತು ಅದರ ಪರಿಭಾಷೆ, ಲ್ಯಾಬ್ ಮೌಲ್ಯಗಳು ಹಾಗೂ ವೈದ್ಯರೊಂದಿಗೆ ಚರ್ಚಿಸಬೇಕಾದ ಪ್ರಶ್ನೆಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಿ."),
    "hi": ("अपने स्वास्थ्य को समझें। अपनी भाषा में।",
           "मेडिकल रिपोर्ट अपलोड करें और उसकी शब्दावली, लैब मानों और डॉक्टर से पूछने योग्य प्रश्नों को समझें।"),
}
title, subtitle = HERO[lang]

st.markdown(f"""<div class="med-hero"><h1>🩺 {title}</h1><p>{subtitle}</p></div>""",
            unsafe_allow_html=True)

c1, c2, c3 = st.columns([2, 1, 1])
with c1:
    if st.button("🔍 Analyze My Report", type="primary", use_container_width=True):
        st.switch_page("pages/2_Upload_Analyze.py")
with c2:
    if st.button("🎯 Try Demo Report", use_container_width=True):
        st.session_state["demo_mode"] = True
        st.switch_page("pages/2_Upload_Analyze.py")
with c3:
    language_selector("main")

st.markdown("### ✨ Feature highlights")
f1, f2, f3, f4 = st.columns(4)
with f1: feature_card("📤", "Smart Upload", "PDF & image reports with signature validation and extraction review.")
with f2: feature_card("🤖", "Gemini AI", "Simple explanations with retry, timeouts, and demo mode.")
with f3: feature_card("🌐", "3 Languages", "English, ಕನ್ನಡ, हिन्दी with bilingual view.")
with f4: feature_card("🔒", "Privacy-first", "Session-only by default. Explicit consent before AI processing.")

st.markdown("### 🪜 How It Works")
st.markdown("""<div class="med-steps">
<div class="med-step"><div class="n">1</div><b>Upload</b><br><span class="med-muted">PDF / PNG / JPG</span></div>
<div class="med-step"><div class="n">2</div><b>Verify</b><br><span class="med-muted">Review extracted values</span></div>
<div class="med-step"><div class="n">3</div><b>Understand</b><br><span class="med-muted">Simple explanations</span></div>
<div class="med-step"><div class="n">4</div><b>Discuss</b><br><span class="med-muted">Questions for your doctor</span></div>
</div>""", unsafe_allow_html=True)

st.markdown("### 🕘 Recent reports")
history = st.session_state.get("report_history", [])
if history:
    for h in history[-3:][::-1]:
        st.markdown(f'<div class="med-card">📄 <b>{h.get("name","Report")}</b> — '
                    f'<span class="med-muted">{h.get("date","")}</span></div>',
                    unsafe_allow_html=True)
else:
    st.info("No saved reports yet. Your session is private by default — save explicitly to see history here.")

st.markdown("###")
disclaimer_box(DISCLAIMER_EN)
st.caption("This is an educational tool, not a medical device. Always consult a qualified clinician.")
