from flask import request, jsonify
from const import SUBSCRIPTION_TIERS, SUBSCRIPTION_HEADER
import tiktoken


def token_count(encoder_for_model: str = "cl100k_base"):
    if request.method == "POST":
        max_tokens = SUBSCRIPTION_TIERS.get(
            request.headers.get(SUBSCRIPTION_HEADER), 128
        )
        max_tokens = max(max_tokens, 128)
        encoding = tiktoken.get_encoding(encoder_for_model)
        token_count = len(encoding.encode(request.json.get("prompt")))
        if token_count > max_tokens:
            return (
                jsonify(
                    {
                        "error": f"Token limit exceeded, max tokens allowed is {max_tokens}"
                    }
                ),
                400,
            )
        else:
            pass
    pass
