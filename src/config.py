import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv


class Config:
    AZURE_AI_API_KEY = os.getenv("AZURE_AI_API_KEY")
    AZURE_AI_API_VERSION = os.getenv("AZURE_AI_API_VERSION")
    AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")

    # Define the name of the header to verify in the request to match subscription tiers
    SUBSCRIPTION_HEADER = "X-Tier"

    # Define the dictionary with subscription tiers and token limits
    SUBSCRIPTION_TIERS = {"free": 124, "basic": 248, "premium": 512, "enterprise": 1024}

    # Define the list of accepted content types
    ACCEPTED_CONTENT_TYPES = ["application/json; charset=utf-8"]

    @staticmethod
    def create_app():
        # Load the environment variables
        load_dotenv()
        app = Flask(__name__)
        # importing the blueprint from the controllers module
        from controllers.prompt import prompt_blueprint
        from controllers.health import health_blueprint

        # importing the middlewares from the middlewares module
        # TODO after initial testing
        # from middlewares import token_count, inspect_headers
        # app.before_request(inspect_headers.check_utf8_encoding)
        # app.before_request(inspect_headers.check_tier_subscription_header)
        app.register_blueprint(prompt_blueprint, url_prefix="/api/v1")
        app.register_blueprint(health_blueprint, url_prefix="/api/v1")
        return app
