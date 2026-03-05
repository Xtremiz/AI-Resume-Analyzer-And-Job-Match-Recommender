import streamlit as st
from SRC.extractor import extract_text_from_pdf,emailextractor
import requests

st.title("Resume Analyzer")
file = st.file_uploader("Enter your Resume",type=["pdf","txt"])

if file is not None:
    st.success("Your pdf is been uploaded")
    text = extract_text_from_pdf(file)
    email = emailextractor(text)
    
else:
    st.warning("please upload the .pdf file")

if st.button("Submit") and file is not None:
 
    with st.spinner("Analyzing Resume..."):
        try:
            api_url = "http://127.0.0.1:8000/post-to-webhook"

            response = requests.post(
                api_url,
                json={
                    "text": text,
                    "email": email   
                }
            )

            if response.status_code == 200:
                result = response.json()

                st.success("Analysis Completed!")

                st.subheader("Extracted Email (Local):")
                st.write(email)

                st.subheader("Analysis Information:")
                st.write(result)

            else:
                st.error(f"API Error: {response.status_code}")

        except Exception as e:
            st.error(f"Something went wrong: {str(e)}")