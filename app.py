
import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. Direct API Configuration - Isse error nahi aayega
API_KEY = "AIzaSyD1GRiJQNvpLdYyyljoFaRkexlBS8-LOAI"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. Page Setup
st.set_page_config(page_title="Ad-Vantage AI 2026", layout="wide")
st.title("🚀 Ad-Vantage AI: Digital Marketing Guru")
st.markdown("---")

# 3. Features Tabs
tab1, tab2, tab3 = st.tabs(["🔍 Ad Analysis", "💡 Viral Ideas", "🛡️ Safety Check"])

with tab1:
    st.header("Ad Post-Mortem (Analysis)")
    uploaded_file = st.file_uploader("Apna Ad Image upload karein...", type=["jpg", "png", "jpeg"])
    platform = st.selectbox("Kahan chalana hai?", ["Instagram Reels", "Facebook", "LinkedIn", "Pinterest"])

    if uploaded_file and st.button("Analyze Now"):
        with st.spinner('AI dimaag laga raha hai...'):
            img = Image.open(uploaded_file)
            st.image(img, width=400, caption="Aapka Ad")
            
            # Special 2026 Prompt
            prompt = f"""
            Analyze this {platform} ad image for the year 2026.
            1. Trust Score: Give a score out of 10.
            2. Vibe Check: Is it 'AI Slop' (fake) or 'Human-centered' (authentic)?
            3. 2026 Hooks: Give 3 viral hooks based on 2026 trends.
            4. Strategy: Does it use 'Before-After' or 'Problem-Solution' logic? How to improve it?
            Keep the response respectful, professional, and witty.
            """
            
            try:
                response = model.generate_content([prompt, img])
                st.success("Analysis Complete!")
                st.markdown("### 📊 AI Report:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")

with tab2:
    st.header("Creative Brainstorming")
    product = st.text_input("Aapka Product ya Service kya hai?")
    if product and st.button("Generate Viral Concepts"):
        concept_prompt = f"Give 3 unique ad concepts for {product} in 2026. Include one 'Funny' and one 'Emotional' hook."
        res = model.generate_content(concept_prompt)
        st.write(res.text)

with tab3:
    st.header("Brand Safety Shield")
    st.info("Hum scan karte hain ki aapka ad platform policies ke hisaab se safe hai ya nahi. (Feature coming soon!)")

st.sidebar.markdown("### 🛠️ Dev Team: Tum + AI")
st.sidebar.success("API Key Connected!")
