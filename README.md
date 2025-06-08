# 🧠 LangChain Ollama Conversational Agent

A modular, production-grade conversational agent built with **LangChain**, **Ollama**, and **Streamlit**. It supports tool-augmented reasoning with DuckDuckGo search, live weather, and current date retrieval.

---

## 🚀 Features

- 🔍 DuckDuckGo-powered web search
- 🌦️ Real-time weather via wttr.in
- 📅 Date retrieval
- 💬 Context-aware chat with multi-turn memory
- 🧠 Thought → Action → Observation trace in sidebar
- 🛠️ Modular tool design (easily extendable)
- ⚙️ Powered by local Ollama + Mistral
- 🖥️ Streamlit frontend

---

## 🖼️ Preview

> Ask things like:

- `Who is Namo?`
- `What is the weather in Redmond today?`
- `What is today's date?`
- `Search for top AI startups in India`

And see the agent's full reasoning trace in the sidebar.

---

## 🧰 Prerequisites

- Python 3.8+
- [Ollama](https://ollama.com) installed locally
- `mistral` model downloaded:
  ```bash
  ollama run mistral
  ```

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/langchain-ollama-agent.git
   cd langchain-ollama-agent
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 📚 Dependencies

Key dependencies and their versions:
- langchain==0.3.25
- langchain_community==0.3.24
- langchain_core==0.3.64
- langchain_ollama==0.3.3
- Requests==2.32.3
- streamlit
- ollama

## 🚀 Usage

1. Start the Streamlit app:
   ```bash
   streamlit run streamlit_app.py
   ```

2. Open your browser at `http://localhost:8501`

3. Start chatting with the agent!

## 🛠️ Development

### Project Structure
```
langchain-ollama-agent/
├── app/
│   ├── core/
│   ├── tools/
│   ├── __init__.py
│   ├── agent.py
│   ├── config.py
│   └── session_manager.py
├── __init__.py
├── streamlit_app.py
├── requirements.txt
├── render.yaml
├── .gitignore
└── README.md
```

### Adding New Tools

1. Create a new tool in `app/tools/`
2. Register it in `app/agent.py`
3. Update the system prompt in `app/core/prompt.py`

The agent is pre-configured using a Python class in app/config.py. No .env file is needed.
# app/config.py

class AgentConfig:
    model_name = "mistral"
    temperature = 0.1
    max_iterations = 5
    host = "http://localhost:11434"
    timeout = 60

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 🙏 Acknowledgments

- [LangChain](https://github.com/langchain-ai/langchain)
- [Ollama](https://github.com/ollama/ollama)
- [Streamlit](https://github.com/streamlit/streamlit)
