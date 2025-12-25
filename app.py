import os
import streamlit as st

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="NeuroCare Africa",
    page_icon="🧠",
    layout="wide",
)

# -----------------------------
# Helpers
# -----------------------------
def show_logo(path: str, width: int = 120):
    if os.path.exists(path):
        st.image(path, width=width)
    else:
        st.caption("Logo not found yet. Add it later at: assets/logos/nch_logo.png")

def disclaimer_block():
    st.warning(
        "Educational use only. This platform does not provide medical advice, diagnosis, or treatment. "
        "If symptoms feel urgent or severe, seek emergency care immediately."
    )

# -----------------------------
# Sidebar (Brand + Governance)
# -----------------------------
with st.sidebar:
    st.title("NeuroCare Africa")
    st.caption("Making brain health knowledge accessible to everyone.")

    st.markdown("---")
    st.subheader("Governance")
    st.markdown(
        "**Sponsored by:** Neuroscience Collaboration Hub (NCH)\n\n"
        "**Founder & Project Lead:** Joseph Duruh\n\n"
        "**NCH Co-Founders:** Joseph Duruh, Ashika Sharma\n\n"
        "**Supported by:**\n"
        "- African Brain Data Network (ABDN) — Dr. Ebere Wogu (General Director)\n"
        "- Youth Neuroscience Association of Nigeria (YNAN) — Dr. Chinna Orish (Founder)\n"
    )

    st.markdown("---")
    st.subheader("Quick Links")
    st.markdown(
        "- Brain Warning Signs\n"
        "- What To Do Now\n"
        "- Brain Wellness\n"
        "- Myth vs Fact\n"
        "- About NeuroCare\n"
    )

# -----------------------------
# Main Home Page
# -----------------------------
left, right = st.columns([2, 1], gap="large")

with left:
    st.markdown("# 🧠 NeuroCare Africa")
    st.markdown(
        "### Neuroscience for everyone — clear, practical, and community-focused.\n\n"
        "NeuroCare Africa is an educational brain health awareness initiative designed to help people:\n"
        "- Recognize early warning signs of neurological emergencies\n"
        "- Learn immediate, safe actions to take\n"
        "- Understand everyday habits that protect brain health\n"
        "- Separate myths from facts with simple explanations\n"
    )
    disclaimer_block()

    st.markdown("## What you can explore")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.info("**Brain Warning Signs**\n\nStroke, seizures, head injury red flags, and when to act fast.")
    with c2:
        st.info("**What To Do Now**\n\nSimple steps you can take while seeking professional care.")
    with c3:
        st.info("**Brain Wellness**\n\nSleep, stress, blood pressure, movement, and prevention education.")

    st.markdown("## Why this matters")
    st.write(
        "Brain-related emergencies can be time-sensitive. Clear knowledge can reduce panic, "
        "support faster decisions, and encourage early medical help. "
        "This project focuses on education that is easy to understand and share."
    )

with right:
    st.markdown("## Today’s Brain Tip")
    tips = [
        "Prioritize sleep — your brain consolidates memory while you rest.",
        "Know FAST signs of stroke: Face drooping, Arm weakness, Speech difficulty, Time to call for help.",
        "High blood pressure can silently raise stroke risk — check it regularly.",
        "Hydration matters — dehydration can worsen headaches and concentration.",
        "Consistent movement supports brain health and mood.",
    ]
    st.success(tips[st.session_state.get("tip_idx", 0) % len(tips)])

    colA, colB = st.columns(2)
    if colA.button("New tip"):
        st.session_state["tip_idx"] = st.session_state.get("tip_idx", 0) + 1
        st.rerun()
    colB.button("Share tip (copy)", help="Long-press or copy from the tip box above.")

# Footer
st.markdown("---")
st.caption(
    "NeuroCare Africa is an initiative of the Neuroscience Collaboration Hub (NCH), co-founded by Joseph Duruh and Ashika Sharma. "
    "Supported by African Brain Data Network (ABDN) and Youth Neuroscience Association of Nigeria (YNAN)."
)
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
# If this code is inside pages/*, BASE_DIR is /pages
# so we go one step up:
ROOT_DIR = BASE_DIR.parent if BASE_DIR.name == "pages" else BASE_DIR

st.markdown("---")
st.subheader("Supported by")

c1, c2, c3 = st.columns([1, 1, 1])

with c1:
    st.image(str(ROOT_DIR / "assets" / "logos" / "nch_logo.png"), use_container_width=True)
    st.caption("Neuroscience Collaboration Hub (NCH)")

with c2:
    st.image(str(ROOT_DIR / "assets" / "logos" / "ABDN.png"), use_container_width=True)
    st.caption("African Brain Data Network (ABDN)")

with c3:
    st.image(str(ROOT_DIR / "assets" / "logos" / "ynan.jpeg"), use_container_width=True)
    st.caption("Youth Neuroscience Association of Nigeria (YNAN)")
