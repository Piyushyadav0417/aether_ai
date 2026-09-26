from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import handle_chat
from app.services.ai_service.providers.openai import OpenAIProvider


router = APIRouter()

provider = OpenAIProvider()


@router.post("/chat")
async def chat(request: ChatRequest) -> ChatResponse:
    return await handle_chat(
        request=request,
        provider=provider
    )