# Akuma Pedia - Devil Fruit Encyclopedia Chatbot

An interactive, AI-powered chatbot that answers questions about Devil Fruits from the One Piece universe. Built with Streamlit and OpenAI's GPT-3.5, this app delivers accurate, conversational responses about fruit types, users, abilities, and lore in real time.

## Features

- Chat interface using Streamlit's `st.chat_message`
- Remembers entire conversation (chat history)
- Uses OpenAI GPT-3.5 with streaming responses
- Specializes in Devil Fruit knowledge only
- Secure API key handling with `.env`

## Tech Stack

- Streamlit: Web-based UI
- OpenAI GPT-3.5 Turbo: Chat model
- dotenv: Secure environment variable management

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/mrp2003/akumapedia
cd akumapedia
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set your OpenAI API key
Create a `.env` file:


```bash
OPENAI_API_KEY=your_openai_key
```
## Usage
```bash
streamlit run app.py
```

Ask questions like:

- "What is the Gomu Gomu no Mi?"
- "Who used the Yami Yami no Mi?"
- "What are the Logia fruits?"

See responses in a fully styled chat interface.

## Contributing
Pull requests are welcome! For major changes, open an issue to discuss improvements.
If you find this project useful, feel free to ⭐ the repository.

