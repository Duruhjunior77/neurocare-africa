import streamlit as st

st.title("Brain Wellness")
st.caption("Daily habits that support brain health over time.")

st.info(
    "These are general education tips. For personal health decisions, speak with a qualified professional."
)

st.subheader("1) Sleep")
st.markdown(
    "- Aim for consistent sleep and wake times\n"
    "- Poor sleep can worsen mood, memory, and concentration\n"
)

st.subheader("2) Blood pressure awareness")
st.markdown(
    "- High blood pressure is a major risk factor for stroke\n"
    "- Check it regularly and follow professional guidance\n"
)

st.subheader("3) Stress and mental wellbeing")
st.markdown(
    "- Chronic stress affects mood, sleep, and focus\n"
    "- Try: breathing routines, journaling, movement, support systems\n"
)

st.subheader("4) Movement")
st.markdown(
    "- Regular activity supports mood and brain function\n"
    "- Start small: walking, stretching, light workouts\n"
)

st.subheader("5) Nutrition & hydration")
st.markdown(
    "- Balanced meals support energy and cognition\n"
    "- Hydration helps reduce fatigue and headaches\n"
)

st.subheader("Quick self-check (non-diagnostic)")
st.slider("Sleep quality (self-rated)", 0, 10, 5)
st.slider("Stress level (self-rated)", 0, 10, 5)
st.slider("Daily movement (self-rated)", 0, 10, 5)
st.caption("These sliders are for reflection only, not diagnosis.")
