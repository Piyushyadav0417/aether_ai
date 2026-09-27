# Aether AI

Aether AI is a backend-focused AI engineering project built with FastAPI.

The project is being developed incrementally, starting with a simple AI chat backend and a clean architecture that separates API handling, application logic, AI services, and LLM providers.

## Features

- FastAPI backend
- AI-powered chat endpoint
- OpenAI Responses API integration
- Provider abstraction for future LLM providers
- Typed request and response contracts using Pydantic
- Environment-based configuration
- Centralized AI error handling
- Basic health check endpoint

## Tech Stack

- Python
- FastAPI
- Pydantic
- Pydantic Settings
- Uvicorn
- OpenAI API

## Project Structure

```text
aether_ai/
│
├── app/
│   ├── api/
│   │   ├── health.py
│   │   └── chat.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   └── exception_handlers.py
│   │
│   ├── schemas/
│   │   └── chat.py
│   │
│   ├── services/
│   │   ├── chat_service.py
│   │   └── ai_service/
│   │       ├── base.py
│   │       ├── exceptions.py
│   │       └── providers/
│   │           └── openai.py
│   │
│   └── main.py
│
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
└── ...
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Piyushyadav0417/aether_ai.git
cd aether_ai
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows PowerShell**

```powershell
.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```
