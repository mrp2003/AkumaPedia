# Developer Guide
This guide explains the full Streamlit + OpenAI chatbot app logic, ideal for beginners or contributors.

## 1. Environment Setup
```python
from dotenv import load_dotenv
import os
```
Loads environment variables from `.env` and reads `OPENAI_API_KEY`.

## 2. OpenAI Client Initialization
```python
from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
```

Initializes the OpenAI SDK client securely.

## 3. Streamlit Configuration
```python
st.set_page_config(page_title="Devil Fruit Encyclopedia", page_icon="logo.png", layout="wide")
st.title("Devil Fruit Encyclopedia Chatbot")
st.markdown("Ask anything about Devil Fruits from the One Piece universe!")
```
Sets up the page, title, and introductory instructions.

## 4. Chat History Initialization
```python
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
```
Ensures conversation state is saved between reruns.
## 5. Message Rendering
```python
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
```
Displays all previous messages using role-based chat bubbles.
## 6. Chat Input Box
```python
user_input = st.chat_input("Ask about any Devil Fruit...")
```
Adds a chat box at the bottom of the screen.

## 7. User Message Handling
```python
st.session_state.chat_history.append({"role": "user", "content": user_input})
```
Appends user question to chat history.

## 8. Compose Prompt + System Role
```python
messages = [{"role": "system", "content": "You are a One Piece expert..."}] + st.session_state.chat_history
```
Adds a system-level instruction to guide GPT’s behavior.

## 9. GPT-3.5 Streaming Response
```python
response = client.chat.completions.create(..., stream=True)
```
Uses OpenAI's stream feature to simulate live typing.

## 10. Save Assistant Reply
```python
st.session_state.chat_history.append({"role": "assistant", "content": full_response})
```
Adds the assistant’s answer to history for continuity.

## Final Notes
This project is a great starting point for themed AI chatbots with persistent context and structured prompts. You can adapt it to other fandoms, subjects, or knowledge bases with minimal changes.