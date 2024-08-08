from flask import Flask, request, jsonify
from config import Config
import requests

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)