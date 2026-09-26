class AIServiceError(Exception):
    """Base exception for AI service errors."""


class AIAuthenticationError(AIServiceError):
    """Raised when authentication with the AI provider fails."""


class AITimeoutError(AIServiceError):
    """Raised when an AI provider request times out."""


class AIRateLimitError(AIServiceError):
    """Raised when an AI provider rate limit is exceeded."""