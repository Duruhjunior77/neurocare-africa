import streamlit as st

st.title("Brain Warning Signs")
st.caption("Recognize early signs. Act early. Seek medical help.")

st.warning(
    "Educational use only. If symptoms are severe, sudden, or worsening, seek emergency care immediately."
)

st.subheader("Stroke: FAST")
st.markdown(
    "- **F — Face:** one side drooping?\n"
    "- **A — Arms:** weakness or numbness in one arm?\n"
    "- **S — Speech:** slurred speech or difficulty speaking?\n"
    "- **T — Time:** act fast and get emergency help.\n"
)

st.subheader("Seizure red flags")
st.markdown(
    "- Seizure lasting **more than 5 minutes**\n"
    "- Repeated seizures without full recovery\n"
    "- First-time seizure\n"
    "- Seizure with injury, pregnancy, diabetes, or breathing problems\n"
)

st.subheader("Head injury: danger signs")
st.markdown(
    "- Loss of consciousness, repeated vomiting\n"
    "- Severe headache that worsens\n"
    "- Confusion, drowsiness, weakness, or seizures\n"
    "- Bleeding or clear fluid from nose/ears\n"
)

st.subheader("Memory/cognition red flags (not emergency, but important)")
st.markdown(
    "- Frequent confusion or getting lost in familiar places\n"
    "- Difficulty doing everyday tasks\n"
    "- Major changes in mood/behavior\n"
    "- Gradual worsening over time\n"
)

st.info("If you are unsure, it’s safer to seek professional medical help early.")
