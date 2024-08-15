from flask import request, jsonify
from const import ACCEPTED_CONTENT_TYPES, SUBSCRIPTION_TIERS, SUBSCRIPTION_HEADER


def check_utf8_encoding():
    if request.method == "POST":
        content_type = request.headers.get("Content-Type")
        if content_type not in ACCEPTED_CONTENT_TYPES:
            return jsonify({"error": "Content-type header not accepted"}), 400
        else:
            pass


def check_tier_subscription_header():
    if request.method == "POST":
        try:
            tier = request.headers.get(SUBSCRIPTION_HEADER, type=str).lower()
            if tier is None or tier not in SUBSCRIPTION_TIERS:
                return (
                    jsonify(
                        {"error": "Subscription header must be present as the api-key"}
                    ),
                    400,
                )
        except Exception as e:
            return jsonify({"error": "Subscription header must be present as the api-key"}), 400
    pass
