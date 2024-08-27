from flask import jsonify
from .azure_base_service import AzureBaseService
from models.gpt_turbo.chat_response import ChatResponse


class ChatService(AzureBaseService):
    def __init__(self):
        super().__init__()

    def send_to_ai_service(self, data: str):
        payload = {
            "messages": [
                {
                    "role": "system",
                    "content": "You are an AI recruiter assistant that helps recruiters to find the best candidates for their job openings and create job descriptions.",
                },
                {
                    "role": "user",
                    "content": data,
                },
            ]
        }
        response = self.make_request(payload)
        modified_response = ChatResponse(response).to_dict()
        return jsonify(modified_response, 200)
