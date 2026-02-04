
import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. API Configuration
API_KEY = "AIzaSyD1GRiJQNvpLdYyyljoFaRkexlBS8-LOAI"
genai.configure(api_key=API_KEY)

# Model setup with stable configuration
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 1024,
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

# 2. Page Interface
st.set_page_config(page_title="Ad-Vantage AI 2026", layout="wide")
st.title("🚀 Ad-Vantage AI: Marketing Guru")
st.markdown("---")

# 3. Functional Tabs
tab1, tab2 = st.tabs(["🔍 Ad Analysis", "💡 Viral Ideas"])

with tab1:
    st.header("Ad Post-Mortem")
    uploaded_file = st.file_uploader("Apna Ad Image upload karein...", type=["jpg", "png", "jpeg"])
    platform = st.selectbox("Platform?", ["Instagram", "Facebook", "LinkedIn", "Pinterest"])

    if uploaded_file and st.button("Analyze Now"):
        with st.spinner('AI analyzing your ad...'):
            try:
                # Image ko AI ke liye ready karna
                img = Image.open(uploaded_file)
                st.image(img, width=400, caption="Analyzing...")
                
                # Instruction for AI
                prompt = f"Analyze this marketing ad for {platform} for the year 2026. Give: 1. Trust Score (out of 10). 2. Vibe Check (Authentic vs Fake). 3. 3 Viral Hooks for 2026. 4. Strategic Improvement. Tone: Professional."
                
                # AI Response generate karna
                response = model.generate_content([prompt, img])
                
                if response.text:
                    st.success("Analysis Complete!")
                    st.markdown("### 📊 AI Strategic Report:")
                    st.write(response.text)
                
            except Exception as e:
                # Error ko handle karna taaki app crash na ho
                st.error("⚠️ AI connection error. Please try again in 5 seconds.")
                st.info(f"Technical details: {e}")

with tab2:
    st.header("Viral Concept Generator")
    topic = st.text_input("Product Name:")
    if topic and st.button("Get Ideas"):
        res = model.generate_content(f"Give 3 viral 2026 ad concepts for {topic}.")
        st.write(res.text)

st.sidebar.info("✅ System: 2026 AI Core Active")
