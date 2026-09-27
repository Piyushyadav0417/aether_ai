import logging

from fastapi import Request
from fastapi.responses import JSONResponse

from app.services.ai_service.exceptions import (
    AIServiceError,
    AIAuthenticationError,
    AITimeoutError,
    AIRateLimitError,
)


logger = logging.getLogger(__name__)


async def ai_service_exception_handler(
    request: Request,
    exc: AIServiceError,
):
    logger.exception("AI service error: %s", exc)

    if isinstance(exc, AIAuthenticationError):
        status_code = 500
        message = "AI service authentication failed."

    elif isinstance(exc, AIRateLimitError):
        status_code = 429
        message = "AI service rate limit exceeded."

    elif isinstance(exc, AITimeoutError):
        status_code = 504
        message = "AI service request timed out."

    else:
        status_code = 500
        message = "AI service error."

    return JSONResponse(
        status_code=status_code,
        content={"detail": message},
    )