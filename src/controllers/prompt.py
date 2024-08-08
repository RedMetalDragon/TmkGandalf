from flask import Blueprint, request, jsonify
from ..services.resume import ResumeService

prompt_blueprint = Blueprint('prompt', __name__)

@prompt_blueprint.route('/read-resume', methods=['POST'])
def process_prompt():
    incoming_prompt = request.json.get('prompt')
    response = ResumeService.process_prompt(incoming_prompt)
    return jsonify(response)