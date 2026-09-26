from app.schemas.chat import ChatRequest, ChatResponse

from app.services.ai_service.base import AIProvider, AIRequest


async def handle_chat(
    request: ChatRequest,
    provider: AIProvider
) -> ChatResponse:

    ai_request = AIRequest(
        message=request.message
    )

    ai_response = await provider.get_response(ai_request)

    return ChatResponse(
        response=ai_response.reply
    )