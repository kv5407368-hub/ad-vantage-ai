import streamlit as st
import google.generativeai as genai
from PIL import Image

# DIRECT KEY - Isme koi badlaav mat karna
genai.configure(api_key="AIzaSyD1GRiJQNvpLdYyyljoFaRkexlBS8-LOAI")
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🚀 Ad-Vantage AI: Step 1 Test")

uploaded_file = st.file_uploader("Photo dalo", type=["jpg", "png", "jpeg"])

if uploaded_file and st.button("Check Karo"):
    try:
        img = Image.open(uploaded_file)
        st.image(img, width=300)
        # AI se baat
        response = model.generate_content(["Is photo mein kya hai?", img])
        st.success("Analysis Poora Hua!")
        st.write(response.text)
    except Exception as e:
        st.error(f"Error: {e}")
