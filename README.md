# 🤖 AI Personal Assistant

A lightweight Flask web app that lets you ask questions and summarize emails using a Groq-powered AI model.

## ✨ Features

- Ask general questions through a simple web interface
- Summarize pasted email content in a few sentences
- Built with Python and Flask
- Uses the Groq API for fast AI responses

## 🧠 Tech Stack

- Python
- Flask
- Groq SDK
- python-dotenv
- HTML, CSS, and JavaScript

## 📁 Project Structure

```bash
AI Assistant/
├── app.py
├── AI_Assistant.py
├── .env
├── static/
│   ├── index.css
│   └── index.js
├── templates/
│   └── index.html
└── README.md
```

## 🚀 Setup

1. Create a virtual environment:

```bash
python -m venv .venv
```

2. Activate it:

- Windows:

```bash
.venv\Scripts\activate
```

- macOS/Linux:

```bash
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install flask python-dotenv groq
```

4. Create a `.env` file in the project root and add your Groq API key:

```bash
GROQ_API_KEY=your_api_key_here
```

5. Run the app:

```bash
python app.py
```

Then open your browser at:

```bash
http://127.0.0.1:5000
```

## 📝 How It Works

- The web interface sends user questions to the `/ask` route.
- The email summarizer uses the `/summarize` route.
- The backend calls the AI model through the `AI_Assistant` class.

## 🔐 Notes

- Keep your Groq API key in a `.env` file and do not commit it to version control.
- The app is configured for local development and runs in debug mode by default.

## 💡 Example Use Cases

- Ask for quick explanations or writing help
- Get a short summary of long email threads
- Use as a simple personal productivity assistant

## License

This project is for educational and personal use.
