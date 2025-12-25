import streamlit as st

st.title("Myth vs Fact")
st.caption("Clear science-based corrections, written simply.")

myths = [
    ("“Stroke is always spiritual.”", "Stroke is a medical emergency involving blood flow to the brain. It needs urgent medical care."),
    ("“Seizures mean madness.”", "Seizures are a neurological event. Many causes exist, and people can live normal lives with proper care."),
    ("“Memory loss is always normal aging.”", "Some forgetfulness can happen, but worsening memory and daily function changes should be assessed."),
    ("“High blood pressure is only for older people.”", "Anyone can have high BP. Early checks can prevent complications."),
]

for m, f in myths:
    with st.expander(m):
        st.write(f)

st.info("If you want, we can add a ‘Shareable Cards’ feature next (downloadable images).")
