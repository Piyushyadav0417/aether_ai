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

## Architecture

Aether AI follows a layered architecture where each layer has a specific responsibility:

```text
Client
  ↓
API Layer
  ↓
Chat Service
  ↓
AI Service
  ↓
LLM Provider
  ↓
OpenAI API
```

The API layer handles HTTP requests and responses, the chat service contains application logic, the AI service defines provider-independent contracts, and the provider layer handles communication with a specific LLM provider.

This separation makes it easier to add or switch LLM providers in the future without tightly coupling the application logic to a specific provider.

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

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create your local `.env` file from the provided example:

**Windows PowerShell:**

```powershell
Copy-Item .env.example .env
```

**macOS / Linux:**

```bash
cp .env.example .env
```

Then open `.env` and configure your OpenAI credentials:

```env
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=your_openai_model
```

> **Important:** Never commit `.env` or expose your OpenAI API key publicly. The `.env` file should remain local and `.env.example` should contain only placeholder values.

### 6. Run the server

Start the FastAPI development server:

```bash
uvicorn app.main:app --reload
```

The server will be available at:

```text
http://127.0.0.1:8000
```

## Testing the API

### Swagger UI

FastAPI automatically provides interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

From Swagger UI, you can view and test the available endpoints directly.

### Health Check

Send a `GET` request to:

```text
GET /health
```

You can test it in your browser or with Postman:

```text
http://127.0.0.1:8000/health
```

A successful response confirms that the API is running.

### Chat Endpoint

Send a `POST` request to:

```text
POST /chat
```

Example request body:

```json
{
  "message": "Hello"
}
```

You can test this endpoint using Swagger UI or Postman.

If the OpenAI configuration is valid, the request will flow through the application layers and return an AI-generated response.

## Error Handling

Aether AI uses custom application-level exceptions for AI service failures:

```text
AIServiceError
├── AIAuthenticationError
├── AITimeoutError
└── AIRateLimitError
```

These exceptions are translated into appropriate HTTP responses by the global FastAPI exception handler.

```text
OpenAI SDK Error
       ↓
OpenAI Provider
       ↓
AIServiceError
       ↓
Global Exception Handler
       ↓
Safe HTTP Response
```

Detailed errors are logged server-side while clients receive safe, generic error messages.

## Development

Aether AI is being developed incrementally with a focus on:

- Clean backend architecture
- Provider-independent AI services
- Strong typing and contracts
- Async programming
- Error handling
- Extensibility for multiple LLM providers
- Production-oriented engineering practices

More capabilities and providers will be added incrementally as the project evolves.
