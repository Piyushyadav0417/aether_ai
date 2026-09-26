from pydantic import BaseModel, Field
from abc import ABC, abstractmethod

class AIRequest(BaseModel):
    message: str = Field(min_length=1)
    
class AIResponse(BaseModel):
    reply: str = Field(min_length=1)
    


# All Ai Provider Parent Class    
class AIProvider(ABC):
    @abstractmethod
    async def get_response(self, request: AIRequest) -> AIResponse:
        pass #openAI response logic here