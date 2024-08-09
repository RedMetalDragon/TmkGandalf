import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from middlewares import check_utf8_encoding, check_tier_subscription_header, token_count


class Config:
    AZURE_AI_API_KEY = os.getenv("AZURE_AI_API_KEY")
    AZURE_AI_API_VERSION = os.getenv("AZURE_AI_API_VERSION")
    AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")

    @staticmethod
    def create_app():
        # Load the environment variables
        load_dotenv()
        app = Flask(__name__)
        # importing the blueprint from the controllers module
        from controllers.prompt import prompt_blueprint
        from controllers.health import health_blueprint

        app.before_request(check_utf8_encoding)
        app.before_request(check_tier_subscription_header)
        app.before_request(token_count)
        app.register_blueprint(prompt_blueprint, url_prefix="/api/v1")
        app.register_blueprint(health_blueprint, url_prefix="/api/v1")
        return app
