from flask import Flask, request, jsonify
from config import Config
import os
import requests

if __name__ == "__main__":
    app = Config.create_app()
    debug_enabled = os.getenv("DEBUG_ENABLED", False)
    app.run(debug=debug_enabled)
