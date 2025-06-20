# 🤖 Local AI Agent with LLaMA 3 & Streamlit

A fully local, LangChain-powered AI agent using [🦙 LLaMA 3 via Ollama](https://ollama.com/) running on CPU, with both terminal and Streamlit interfaces.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![LangChain](https://img.shields.io/badge/LangChain-Enabled-blueviolet?logo=chainlink)
![Ollama](https://img.shields.io/badge/Ollama-LLaMA_3-forestgreen?logo=llama)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-orange?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 🚀 Features

- 🔢 **Math Solver** (Python code execution)
- 🔍 **Search Tool** (mocked or extendable to real API)
- 🧠 **LLM-powered Reasoning** using LLaMA 3
- 🌐 **Streamlit Web UI**
- 🖥️ **Fully Offline** & runs on CPU

---

## 📁 Project Structure

local-ai-agent/
├── main.py # CLI Agent
├── app.py # Streamlit Web App
├── requirements.txt # Dependencies
├── .gitignore
└── README.md # You're here!



---

## ⚙️ Setup Instructions

### 🔧 Prerequisites

- Python 3.10+
- Ollama (install from [https://ollama.com](https://ollama.com))
- LLaMA 3 model pulled via `ollama pull llama3`

---

### 🛠️ Install & Run (Windows)

```bash
# 1. Clone repo
git clone https://github.com/yourusername/local-ai-agent.git
cd local-ai-agent

# 2. Create & activate virtual environment
python -m venv env
env\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Pull LLaMA 3 model (if not already done)
ollama pull llama3

# 5. Run terminal agent
python main.py

# OR run Streamlit web app
streamlit run app.py
