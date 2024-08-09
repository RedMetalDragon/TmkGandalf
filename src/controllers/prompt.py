from flask import Blueprint, request, jsonify
from services import chat

prompt_blueprint = Blueprint("prompt", __name__)


@prompt_blueprint.route("/prompt", methods=["POST"])
def process_prompt():
    chat_service = chat.ChatService()
    incoming_prompt = request.json.get("prompt")
    try:
        return chat_service.send_to_ai_service(incoming_prompt)
    except Exception as e:
        return jsonify({"error": str(e)}, 500)
