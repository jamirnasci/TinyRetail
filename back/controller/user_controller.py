from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from models.user import User

user_bp = Blueprint('user', __name__)

@user_bp.route('/create', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    password = data.get('password')

    password = generate_password_hash(password)

    try:
        user = User(name=name, email=email, phone=phone, password=password)
        user.save()
        return jsonify({'msg': 'Usuário criado com sucesso'})
    except Exception as e:
        print(e)
        return jsonify({'msg': 'Falha ao criar usuário'}), 401

