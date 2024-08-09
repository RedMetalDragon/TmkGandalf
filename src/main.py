from flask import Flask, request, jsonify
from config import Config
import requests

if __name__ == "__main__":
    app = Config.create_app()
    app.run(debug=True)