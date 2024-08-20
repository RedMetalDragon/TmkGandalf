class ChoiceResponse():
    def __init__(self, choice: dict):
        self.index = choice.get("index")
        self.finish_reason = choice.get("finish_reason")
        self.message_response = choice.get("message").get("content")
        self.role = choice.get("message").get("role")
    
    def to_dict(self):
        return {
            "index": self.index,
            "finish_reason": self.finish_reason,
            "message_response": self.message_response,
            "role": self.role,
        }