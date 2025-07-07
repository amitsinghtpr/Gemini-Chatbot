import streamlit as st
from memory import Memory
from chatbot import Chatbot
from utils import validate_input, format_response
from PyPDF2 import PdfReader
from PIL import Image

st.set_page_config(page_title="KIRAN - Gemini Chatbot", page_icon="🤖")

# Initialize memory and chatbot
if "memory" not in st.session_state:
    st.session_state.memory = Memory()
if "chatbot" not in st.session_state:
    st.session_state.chatbot = Chatbot(st.session_state.memory, model="gemini-1.5-flash")
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("🤖 KIRAN - Gemini Chatbot")

# File upload for PDF or Image
uploaded_file = st.file_uploader("Upload a PDF or Image for reference (optional)", type=["pdf", "png", "jpg", "jpeg"])

# Extract text from PDF or image (simple OCR for images)
def extract_file_text(file):
    if file is None:
        return ""
    if file.type == "application/pdf":
        pdf_reader = PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() or ""
        return text.strip()
    elif file.type.startswith("image/"):
        try:
            import pytesseract
            image = Image.open(file)
            return pytesseract.image_to_string(image)
        except ImportError:
            st.warning("Install pytesseract for image OCR support.")
            return ""
    return ""

file_context = extract_file_text(uploaded_file)

# Chat UI
st.markdown(
    """
    <style>
    .main {
        background-color: #18191A;
    }
    .chat-container {
        display: flex;
        flex-direction: column;
        gap: 12px;
        margin-top: 24px;
    }
    .user-msg {
        background: linear-gradient(90deg, #43e97b 0%, #38f9d7 100%);
        color: #222;
        padding: 12px 18px;
        border-radius: 18px 18px 4px 18px;
        align-self: flex-end;
        max-width: 70%;
        font-size: 1.1em;
        font-weight: 500;
        box-shadow: 0 2px 8px rgba(67,233,123,0.08);
    }
    .bot-msg {
        background: linear-gradient(90deg, #434343 0%, #262626 100%);
        color: #f8f8f8;
        padding: 12px 18px;
        border-radius: 18px 18px 18px 4px;
        align-self: flex-start;
        max-width: 70%;
        font-size: 1.1em;
        font-weight: 400;
        box-shadow: 0 2px 8px rgba(67,233,123,0.08);
    }
    .bot-name {
        font-weight: bold;
        color: #43e97b;
        font-size: 1.05em;
        margin-bottom: 2px;
        display: block;
    }
    </style>
    """, unsafe_allow_html=True
)

chat_container = st.container()
with chat_container:
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for sender, msg in st.session_state.chat_history:
        if sender == "user":
            st.markdown(f'<div class="user-msg">{msg}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="bot-msg"><span class="bot-name">KIRAN</span>{msg}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Replace your input and send logic with this:

def handle_send():
    user_input = st.session_state.input.strip()
    if not user_input:
        return
    st.session_state.chat_history.append(("user", user_input))
    context = f"{file_context}\n\n{user_input}" if file_context else user_input
    try:
        validated_input = validate_input(context)
        response = st.session_state.chatbot.generate_response(validated_input)
        formatted = format_response(response)
        st.session_state.chat_history.append(("bot", formatted))
    except Exception as e:
        st.session_state.chat_history.append(("bot", f"Error: {e}"))
    # Clear input by setting to empty string
    st.session_state.input = ""

# Input box with ENTER to send, using on_change callback
st.text_input(
    "Type your message and press ENTER",
    key="input",
    on_change=handle_send
)

# Button to clear chat
if st.button("Clear Chat"):
    st.session_state.chat_history = []
    st.session_state.memory.clear_memory()
    st.rerun()