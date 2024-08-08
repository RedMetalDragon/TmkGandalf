import os
from flask import Flask, request, jsonify


class Config:
    AZURE_AI_API_KEY = os.getenv("AZURE_AI_API_KEY")
    AZURE_AI_API_VERSION = os.getenv("AZURE_AI_API_VERSION")
    AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
    
    #Define the name of the header to verify in the request to match subscription tiers
    SUBSCRIPTION_HEADER = "X-Tier"

    # Define the dictionary with subscription tiers and token limits
    SUBSCRIPTION_TIERS = {"free": 124, "basic": 248, "premium": 512, "enterprise": 1024}

    # Define the list of accepted content types
    ACCEPTED_CONTENT_TYPES = ["application/json; charset=utf-8"]

    def create_app():
        app = Flask(__name__)
        app.register_blueprint(
            "api", url_prefix="/api"
        )  # TODO: Implement the API blueprint
        return app
