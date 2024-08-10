from config import Config
import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from middlewares import check_utf8_encoding, check_tier_subscription_header, token_count
import requests


def create_app():
    # Load the environment variables
    load_dotenv()
    app = Flask(__name__)

    # Importing the blueprints from the controllers module
    from controllers.prompt import prompt_blueprint
    from controllers.health import health_blueprint

    # Register middlewares
    app.before_request(check_utf8_encoding)
    app.before_request(check_tier_subscription_header)
    app.before_request(token_count)

    # Register blueprints
    app.register_blueprint(prompt_blueprint, url_prefix="/api/v1")
    app.register_blueprint(health_blueprint, url_prefix="/api/v1")

    return app

# Create the app (global scope)
app = create_app()

if __name__ == "__main__":    
    debug_enabled = os.getenv("DEBUG_ENABLED", False)
    app.run(debug=debug_enabled)
