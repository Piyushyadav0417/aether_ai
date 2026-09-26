from ai_service.base import AIRequest, AIResponse, AIProvider

class OpenAIProvider(AIProvider):
    async def get_response(self, request):
        pass