import streamlit as st
import google.generativeai as genai
from PIL import Image

# Sabse fresh key jo aapne abhi banayi hai
genai.configure(api_key="AIzaSyDLHcqfApzr7f1SW1D9yPw3_ZcGJVEkMpg")
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🚀 Ad-Vantage AI: Connection Test")

file = st.file_uploader("Upload any image", type=["jpg", "png", "jpeg"])

if file:
    img = Image.open(file)
    st.image(img, width=300)
    if st.button("Analyze Now"):
        try:
            # Seedha connection test
            res = model.generate_content(["What is in this image?", img])
            st.success("Connection Done!")
            st.write(res.text)
        except Exception as e:
            st.error(f"Error: {e}")
