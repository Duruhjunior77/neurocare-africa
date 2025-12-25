import streamlit as st

st.title("What To Do Now")
st.caption("Simple, safe actions while seeking medical help.")

st.warning(
    "Educational use only. This page does not replace emergency services or professional medical advice."
)

st.subheader("If you suspect stroke")
st.markdown(
    "- Keep the person safe and calm\n"
    "- Note the **time symptoms started**\n"
    "- Do **not** give food or drink if swallowing is difficult\n"
    "- Seek urgent medical care immediately\n"
)

st.subheader("If someone is having a seizure")
st.markdown(
    "- Place them on their side (recovery position)\n"
    "- Remove sharp objects nearby\n"
    "- Cushion the head, loosen tight clothing\n"
    "- Do **not** put anything in the mouth\n"
    "- Time the seizure if possible\n"
    "- Seek urgent help if it lasts **>5 minutes** or repeats\n"
)

st.subheader("For severe headache or head injury warning signs")
st.markdown(
    "- Seek medical help urgently\n"
    "- Avoid unnecessary movement if neck/spine injury is possible\n"
    "- Monitor alertness and breathing\n"
)

st.subheader("What to tell a clinician (helps faster care)")
st.markdown(
    "- What happened and **when it started**\n"
    "- Symptoms and how they changed\n"
    "- Any known conditions (BP, diabetes), medications\n"
    "- Any recent injury, infection, or substance use\n"
)
