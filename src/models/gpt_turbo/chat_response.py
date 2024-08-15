import collections
from .chat_choice import ChoiceResponse

class ChatResponse:
    def __init__(self, response: dict):
        self.response = response
        self.chat_id = response.get("id")
        self.usage = response.get("usage")
        self.object = response.get("object")
        self.choices = response.get("choices")

    def map_usage(self, usage) -> dict:
        usage = {}
        try:
            for key, value in usage.items():
                usage.__setattr__(key, value)
        except Exception as e:
            print(f"Error mapping usage: {e}")
        return usage

    def map_choices(self) -> list[ChoiceResponse]:
        choices_stack = collections.deque()
        try:
            for value in sorted(self.choices, key=lambda x: x.get("index")):
                choices_stack.append(ChoiceResponse(choice=value))
            return choices_stack
        except Exception as e:
            print(f"Error mapping choices: {e}")
            return collections.deque()

    def to_dict(self):
        return {
            "chat_id": self.chat_id,
            "usage": [choice.to_dict() for choice in self.map_choices()],
        }