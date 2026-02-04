import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="Ad-Vantage AI 2026", layout="wide")
st.title("🚀 Ad-Vantage AI: Digital Marketing Guru")

# Sidebar for API Key
api_key = st.sidebar.text_input("Apni Gemini API Key yahan dalein:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    tab1, tab2, tab3 = st.tabs(["🔍 Ad Analysis", "💡 Viral Ideas", "🛡️ Safety Check"])

    with tab1:
        st.header("Ad Post-Mortem")
        uploaded_file = st.file_uploader("Apna Ad (Image) upload karein...", type=["jpg", "png", "jpeg"])
        platform = st.selectbox("Platform select karein:", ["Instagram Reels", "Facebook", "LinkedIn", "Pinterest"])

        if uploaded_file and st.button("Analyze Now"):
            img = Image.open(uploaded_file)
            st.image(img, width=300)
            
            prompt = f"Analyze this {platform} ad for 2026. Give Trust Score, 3 Viral Hooks, and check if it uses Problem-Solution or Before-After logic. Tone: Respectful & Professional."
            response = model.generate_content([prompt, img])
            st.markdown(response.text)

    with tab2:
        st.header("Creative Brainstorming")
        topic = st.text_input("Product ka naam?")
        if topic and st.button("Generate Concepts"):
            res = model.generate_content(f"Give 3 unique ad concepts for {topic} in 2026 including a funny and an emotional hook.")
            st.write(res.text)

    with tab3:
        st.header("Brand Safety Shield")
        st.info("Hum scan karte hain ki aapka ad policy safe hai ya nahi.")
else:
    st.warning("Pehle Sidebar mein apni API Key daalein.")
