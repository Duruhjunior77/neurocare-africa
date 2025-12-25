import streamlit as st
from pathlib import Path
from datetime import date
import random

# -----------------------------
# PAGE CONFIG (mobile + PC)
# -----------------------------
st.set_page_config(
    page_title="NeuroCare Africa",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed",  # better on mobile
)

# -----------------------------
# PATHS
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent if BASE_DIR.name == "pages" else BASE_DIR

LOGO_NCH = ROOT_DIR / "assets" / "logos" / "nch_logo.png"
LOGO_ABDN = ROOT_DIR / "assets" / "logos" / "ABDN.png"
LOGO_YNAN = ROOT_DIR / "assets" / "logos" / "ynan.jpeg"

# -----------------------------
# MOBILE-FRIENDLY CSS
# -----------------------------
st.markdown(
    """
<style>
/* reduce padding for better mobile fit */
.block-container {padding-top: 1.0rem; padding-bottom: 1.2rem;}
@media (max-width: 768px){
  .block-container {padding-left: 0.9rem; padding-right: 0.9rem;}
}

/* nicer headings */
h1, h2, h3 {letter-spacing: -0.2px;}
.small-note {opacity: 0.85; font-size: 0.92rem;}

/* card-like containers */
.card {
  padding: 14px 14px;
  border: 1px solid rgba(49, 51, 63, 0.15);
  border-radius: 12px;
  background: rgba(255, 255, 255, 0.02);
}

/* footer logos align */
.footer-caption {text-align:center; margin-top:6px; opacity:0.85; font-size:0.9rem;}
</style>
""",
    unsafe_allow_html=True,
)

# -----------------------------
# HEADER (no sidebar logo)
# -----------------------------
top_left, top_right = st.columns([1, 3], vertical_alignment="center")

with top_left:
    # Header logo: show only if file exists
    if LOGO_NCH.exists():
        st.image(str(LOGO_NCH), width=90)
    else:
        st.write("🧠")

with top_right:
    st.title("NeuroCare Africa")
    st.markdown(
        "<div class='small-note'>Practical, accessible brain-health education for everyone.</div>",
        unsafe_allow_html=True,
    )

st.markdown("")

# -----------------------------
# MAIN CONTENT (mobile-friendly single column, then optional split)
# -----------------------------
st.markdown(
    """
<div class="card">
<b>What this is:</b> A community-focused brain health resource hub.  
<b>What this is not:</b> A medical diagnosis or emergency service.
</div>
""",
    unsafe_allow_html=True,
)

st.markdown("")

# On desktop, two columns look good; on mobile Streamlit will stack them automatically.
col_a, col_b = st.columns([2, 1], gap="large")

with col_a:
    st.subheader("Start here")
    st.write(
        "Explore simple, science-informed guidance on brain warning signs, what to do next, "
        "healthy habits, and common myths. Use the sidebar to open each page."
    )

    st.markdown("**Quick links (use sidebar too):**")
    st.write("- Brain Warning Signs")
    st.write("- What To Do Now")
    st.write("- Brain Wellness")
    st.write("- Myth vs Fact")
    st.write("- About NeuroCare")

with col_b:
    st.subheader("Today’s Brain Tip")
    tips = [
        "Sleep is brain maintenance. Aim for consistent sleep and wake times.",
        "Hydration supports focus. Drink water regularly through the day.",
        "Short walks improve mood and attention—10 minutes counts.",
        "Stress is real. Slow breathing for 2 minutes can calm your nervous system.",
        "Learning something new strengthens brain networks over time.",
    ]
    # deterministic daily tip
    random.seed(str(date.today()))
    st.info(random.choice(tips))

st.markdown("")

# -----------------------------
# SAFETY / DISCLAIMER (important)
# -----------------------------
with st.expander("Important note", expanded=False):
    st.write(
        "This tool is for education and awareness only. It does not provide medical advice, "
        "diagnosis, or treatment. If you have severe symptoms (e.g., sudden weakness, "
        "difficulty speaking, seizure, fainting, severe headache, confusion), seek urgent "
        "medical help immediately."
    )

# -----------------------------
# FOOTER: SUPPORTED BY (responsive)
# -----------------------------
from pathlib import Path
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent if BASE_DIR.name == "pages" else BASE_DIR

# ---- Footer: Supported by (ONLY ONCE) ----
st.markdown("---")
st.subheader("Supported by")

# Small CSS so images don’t stretch weirdly (helps blur)
st.markdown(
    """
    <style>
      div[data-testid="stImage"] img {
        image-rendering: auto;
        max-height: 90px;
        width: auto;
      }
    </style>
    """,
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)

with c1:
    st.image(str(ROOT_DIR / "assets" / "logos" / "nch_logo.png"), width=180)
    st.caption("Neuroscience Collaboration Hub (NCH)")

with c2:
    st.image(str(ROOT_DIR / "assets" / "logos" / "ABDN.png"), width=180)
    st.caption("African Brain Data Network (ABDN)")

with c3:
    st.image(str(ROOT_DIR / "assets" / "logos" / "ynan.jpeg"), width=180)
    st.caption("Youth Neuroscience Association of Nigeria (YNAN)")
