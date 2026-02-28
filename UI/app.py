import streamlit as st

st.title("Resume Analyzer")
file = st.file_uploader("Enter your Resume",type=[".pdf"])
if st.button("Submit"):
    pass