from openai import (
    AsyncOpenAI,
    AuthenticationError,
    RateLimitError,
    APITimeoutError,
)

from app.services.ai_service.base import (
    AIRequest,
    AIResponse,
    AIProvider,
)

from app.services.ai_service.exceptions import (
    AIAuthenticationError,
    AITimeoutError,
    AIRateLimitError,
    AIServiceError,
)

from app.core.config import get_settings

class OpenAIProvider(AIProvider):
    
    def __init__(self):
        settings = get_settings()

        self.client = AsyncOpenAI(
            api_key=settings.OPENAI_API_KEY
        )

        self.model = settings.OPENAI_MODEL

    async def get_response(self, request: AIRequest) -> AIResponse:

        try:
            response = await self.client.responses.create(
                model=self.model,
                input=request.message,
            )

            return AIResponse(
                reply=response.output_text
            )

        except AuthenticationError as exc:
            raise AIAuthenticationError(
                "Authentication with OpenAI failed."
            ) from exc

        except RateLimitError as exc:
            raise AIRateLimitError(
                "OpenAI rate limit exceeded."
            ) from exc

        except APITimeoutError as exc:
            raise AITimeoutError(
                "OpenAI request timed out."
            ) from exc
        
        except Exception as exc:
            raise AIServiceError(
                "An unexpected error occured while communicating with OpenAI."
            ) from exc