# 🤖 LocalAIChatbot

A locally running AI chatbot built using **Python, FastAPI, Ollama, and Llama 3.2**.

LocalAIChatbot is a personal AI assistant that allows users to interact with a locally running Large Language Model (LLM). It uses a separate frontend and backend architecture to provide a simple chat experience without relying on a cloud AI API.

## ✨ Features

- 🤖 AI-powered conversations using Llama 3.2
- 💻 Runs locally using Ollama
- ⚡ FastAPI backend for handling chat requests
- 🎨 Modern and responsive chat interface
- 💬 Maintains conversation context during a chat session
- 🗑️ Clear conversation and start a new chat
- 🔌 REST API for frontend-backend communication
- 🔒 No external cloud AI API required

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| FastAPI | Backend API framework |
| Ollama | Running AI models locally |
| Llama 3.2 | Large Language Model |
| HTML | Frontend structure |
| CSS | Frontend styling |
| JavaScript | Frontend functionality |
| Uvicorn | Running the FastAPI server |

## 📁 Project Structure

```text
LocalAIChatbot/
│
├── backend/
│   ├── __init__.py
│   └── main.py
│
├── frontend/
│   ├── index.html
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
├── app.py
├── test.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Maxwell-Thomas/LocalAIChatbot.git
```

### 2. Open the project folder

```bash
cd LocalAIChatbot
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Install and configure Ollama

Download Ollama:

https://ollama.com/download

Pull the Llama 3.2 model:

```bash
ollama pull llama3.2
```

Make sure Ollama is running before starting the application.

## 🚀 Run the Application

Start the FastAPI backend using:

```bash
uvicorn backend.main:app --reload
```

Open your browser and visit:

http://127.0.0.1:8000

Your Local AI Assistant is now ready!

## 🔗 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Loads the chatbot frontend |
| GET | `/api/health` | Checks backend status |
| POST | `/api/chat` | Sends messages to the AI model |

FastAPI interactive API documentation:

http://127.0.0.1:8000/docs

## 🧠 How It Works

1. The user enters a message in the chatbot interface.
2. JavaScript sends the message to the FastAPI backend.
3. FastAPI processes the request.
4. Ollama communicates with the locally running Llama 3.2 model.
5. The AI generates a response.
6. The backend returns the response to the frontend.
7. The chatbot displays the AI response.

## 🎯 Project Objective

The main objective of this project is to understand how locally hosted Large Language Models work and how to integrate them into a web application using Python and REST APIs.

It also demonstrates frontend-backend separation and local AI model integration.

## 👨‍💻 Developer

**Maxwell Thomas**

GitHub: https://github.com/Maxwell-Thomas

---

⭐ If you find this project interesting, consider giving the repository a star!

**Built with Python, Ollama, and curiosity.**