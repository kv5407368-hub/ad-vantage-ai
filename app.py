
import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. FIX: API Key ko seedha yahan fit kar diya hai taaki error na aaye
API_KEY = "AIzaSyD1GRiJQNvpLdYyyljoFaRkexlBS8-LOAI"
genai.configure(api_key=API_KEY)

# Stable Model for 2026 Ads
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. UI Setup
st.set_page_config(page_title="Ad-Vantage AI 2026", layout="wide")
st.title("🚀 Ad-Vantage AI: Marketing Guru")
st.markdown("---")

tab1, tab2 = st.tabs(["🔍 Ad Analysis", "💡 Viral Ideas"])

with tab1:
    st.header("Ad Analysis (2026 Edition)")
    uploaded_file = st.file_uploader("Apna Ad Image upload karein...", type=["jpg", "png", "jpeg"])
    platform = st.selectbox("Kahan chalana hai?", ["Instagram Reels", "Facebook", "LinkedIn", "Pinterest"])

    if uploaded_file and st.button("Analyze Now"):
        with st.spinner('AI Report taiyar kar raha hai...'):
            try:
                # Processing Image
                img = Image.open(uploaded_file)
                st.image(img, width=400, caption="Analyzing your Ad...")
                
                # Instruction to AI
                prompt = f"Analyze this {platform} ad for the year 2026. Give: 1. Trust Score. 2. Is it authentic or fake? 3. 3 Viral Hooks for 2026. 4. Strategic tips. Keep it professional."
                
                # AI Response
                response = model.generate_content([prompt, img])
                
                st.success("Analysis Complete!")
                st.markdown("### 📊 AI Strategic Report:")
                st.write(response.text)
                
            except Exception as e:
                # Agar Google ke server se dikkat ho toh ye dikhayega
                st.error("⚠️ AI Connection Error. Dobara try karein.")
                st.info(f"Details: {e}")

with tab2:
    st.header("Viral Concept Generator")
    product = st.text_input("Product ka naam:")
    if product and st.button("Get Ideas"):
        res = model.generate_content(f"Give 3 viral 2026 ad concepts for {product}.")
        st.write(res.text)

st.sidebar.success("✅ System Connected: 2026 Mode Active")
st.sidebar.info("Aapko ab key daalne ki zaroorat nahi hai.")
