from abc import ABC, abstractmethod

class OpenAIService(ABC):
    
    @abstractmethod
    def send_to_ai_service(self, data: str) -> str:
        pass