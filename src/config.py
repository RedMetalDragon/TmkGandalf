import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from middlewares import check_utf8_encoding, check_tier_subscription_header, token_count


class Config:
    AZURE_AI_API_KEY = os.getenv("AZURE_AI_API_KEY")
    AZURE_AI_API_VERSION = os.getenv("AZURE_AI_API_VERSION")
    AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
