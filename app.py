import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# -------------------------------
# Load API Key from .env
# -------------------------------
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(page_title="Devil Fruit Encyclopedia", page_icon="logo.png", layout="wide")
st.title("Devil Fruit Encyclopedia Chatbot")
st.markdown("Ask anything about Devil Fruits from the One Piece universe!")

# -------------------------------
# Initialize Chat History
# -------------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -------------------------------
# Render Previous Messages
# -------------------------------
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -------------------------------
# Chat Input Box (Fixed Bottom)
# -------------------------------
user_input = st.chat_input("Ask about any Devil Fruit...")

# -------------------------------
# Handle New User Message
# -------------------------------
if user_input:
    # Add user message to chat history
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

# -------------------------------
# Prepare Chat Prompt for GPT
# -------------------------------
    messages = [{"role": "system", "content": (
        "You are a One Piece expert specialized in Devil Fruits. Only answer questions about Devil Fruits, "
        "including their powers, users (past and present), fruit type (Paramecia, Zoan, Logia), origin stories, "
        "famous battles, and known weaknesses. Avoid answering anything unrelated to Devil Fruits."
    )}] + st.session_state.chat_history

# -------------------------------
# Get Assistant Response (Streaming)
# -------------------------------
    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_response = ""
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                stream=True,
                temperature=0.7
            )
            for chunk in response:
                if chunk.choices[0].delta.content:
                    full_response += chunk.choices[0].delta.content
                    placeholder.markdown(full_response + "▌")
            placeholder.markdown(full_response)
        except Exception as e:
            full_response = f"Error: {e}"
            placeholder.markdown(full_response)

    # Save assistant message to chat history
    st.session_state.chat_history.append({"role": "assistant", "content": full_response})
