import os
import streamlit as st
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    st.error("❌ GOOGLE_API_KEY not loaded")
    st.stop()

genai.configure(api_key=API_KEY)

# =============================
# 🎨 PAGE CONFIG
# =============================
st.set_page_config(
    page_title="Generative AI Multimodal Application",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Generative AI Multimodal Application")
st.caption("Text-to-Text & Image-to-Text using Google Gemini")

# =============================
# 📌 TABS
# =============================
tab1, tab2 = st.tabs(["📝 Text to Text", "🖼️ Image to Text"])

# =============================
# 📝 TEXT TO TEXT
# =============================
with tab1:
    st.subheader("📝 Text to Text Chat")

    user_input = st.text_area(
        "Enter your question or prompt",
        placeholder="Ask anything...",
        height=150
    )

    if st.button("Generate Answer 🚀"):
        if user_input.strip():
            with st.spinner("Thinking..."):
                model = genai.GenerativeModel("models/gemini-2.5-flash-preview-09-2025")
                response = model.generate_content(user_input)
                st.success("Response")
                st.write(response.text)
        else:
            st.warning("Please enter some text")

# =============================
# 🖼️ IMAGE TO TEXT
# =============================
with tab2:
    st.subheader("🖼️ Image to Text")

    uploaded_image = st.file_uploader(
        "Upload an image",
        type=["jpg", "jpeg", "png"]
    )

    image_prompt = st.text_input(
        "Ask something about the image",
        placeholder="Describe this image / What is happening here?"
    )

    if uploaded_image:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Analyze Image 🔍"):
            if image_prompt.strip():
                with st.spinner("Analyzing image..."):
                    model = genai.GenerativeModel("models/gemini-2.5-flash-preview-09-2025")
                    response = model.generate_content([image_prompt, image])
                    st.success("Image Analysis Result")
                    st.write(response.text)
            else:
                st.warning("Please enter a prompt for the image")

# =============================
# 📌 FOOTER
# =============================
st.markdown("---")
st.markdown(
    "Built with ❤️ using **Streamlit + Google Gemini**"
)
