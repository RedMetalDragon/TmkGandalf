from flask import request, jsonify
from ..config import Config
import tiktoken


def token_count(request, response, encoder_for_model: str = "cl100k_base"):
    if request.method == "POST":
        encoding = tiktoken.get_encoding(encoder_for_model)
        tier = request.headers.get("X-Tier")
        token_count = len(encoding.encode(request.json.get("prompt")))
        if token_count > Config.SUBSCRIPTION_TIERS[tier]:
            return jsonify({"error": "Token limit exceeded"}), 400
        else:
            pass
    pass
