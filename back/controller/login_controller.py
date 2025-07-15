from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    print(data.get('email'))
    token = create_access_token(identity='1', additional_claims={'user': 'jamir'})
    return jsonify({'msg': 'Login Realizado', 'token': token})