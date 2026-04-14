# 🤖 Streamlit Chatbot with LangGraph (Dynamic LLM Config)

A conversational chatbot built using **Streamlit + LangGraph**, allowing users to dynamically input their **OpenAI API key and model** from the UI.

---

## 🚀 Features

- 💬 ChatGPT-like UI using Streamlit
- 🧠 Stateful conversations using LangGraph
- 🔑 User-provided OpenAI API key (secure, runtime only)
- ⚙️ Dynamic model selection (gpt-4o-mini, gpt-4o, etc.)
- 🧵 Session-based memory using thread_id
- ⚡ Fast and lightweight `uv` project setup
- 🌍 Free deployment ready (Streamlit Cloud)

---

## 🏗️ Project Structure
├── pyproject.toml # uv dependencies
├── uv.lock
├── README.md
│
├── backend_chatbot.py # LangGraph chatbot builder
├── frontend_chatbot.py # Streamlit UI
│
└── .streamlit/
└── config.toml # Streamlit config


---

## ⚙️ Tech Stack

- **Frontend**: Streamlit  
- **Backend**: LangGraph  
- **LLM**: OpenAI (dynamic selection)  
- **Memory**: InMemorySaver (LangGraph)  
- **Dependency Manager**: uv  

---

## 🧠 Architecture Overview

### 🔹 Backend (LangGraph)

- Uses a graph-based workflow:
START → chat_node → END

- Dynamically creates LLM instance using user input
- Maintains conversation state via `thread_id`

---

### 🔹 Frontend (Streamlit)

- Sidebar for:
- API Key input
- Model selection
- Chat UI:
- Displays history
- Handles user input
- Calls backend dynamically

---

## 🔑 Setup Instructions

### 1. Clone Repository

```bash
git clone <your-repo-url>
cd chatbot-uv

