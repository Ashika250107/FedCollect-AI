import streamlit as st
from backend.pipeline import run_pipeline

st.title("Debt Collection AI System")

amount = st.number_input("Outstanding Amount", min_value=0)
risk = st.selectbox("Risk Level", ["Low", "Medium", "High"])

if st.button("Get Recommendation"):
    result = run_pipeline(amount, risk)
    st.success(f"Recommended Action: {result}")
