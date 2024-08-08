from flask import request, jsonify
from ..config import Config


def check_utf8_encoding(request):
    if request.method == "POST":
        content_type = request.headers.get("Content-Type")
        if content_type not in Config.ACCEPTED_CONTENT_TYPES:
            return jsonify({"error": "Content-type header not accepted"}), 400
        else:
            pass


def check_tier_subscription_header(request):
    if request.method == "POST":
        tier = request.headers.get("X-Tier")
        if tier is not None and tier not in Config.SUBSCRIPTION_TIERS:
            return (
                jsonify(
                    {"error": "Subscription header must be present as the api-key"}
                ),
                400,
            )
        else:
            pass
    pass
