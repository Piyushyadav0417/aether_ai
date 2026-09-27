from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.chat import router as chat_router
from app.core.exception_handlers import ai_service_exception_handler
from app.services.ai_service.exceptions import AIServiceError

app = FastAPI()

app.include_router(health_router)
app.include_router(chat_router)

app.add_exception_handler(
    AIServiceError,
    ai_service_exception_handler,
)