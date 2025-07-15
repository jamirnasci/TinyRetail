from flask import Flask, jsonify
from flask_cors import CORS
import jwt
from controller.product_controller import product_bp
from controller.sales_controller import sales_bp
from controller.user_controller import user_bp
from controller.login_controller import login_bp
from controller.supplier_controller import supplier_bp

from flask_jwt_extended import JWTManager

from models.product import Product
from models.sale import Sale
from models.sale_list import SaleList
from models.supplier import Supplier
from models.user import User
from config.db import db
from datetime import timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dmkasmdom2390d23djnnd'
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=8)

CORS(app)

jwt = JWTManager(app)

db.connect()
db.create_tables([Product, Sale, SaleList, Supplier, User])

app.register_blueprint(product_bp, url_prefix='/products')
app.register_blueprint(sales_bp, url_prefix='/sales')
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(login_bp, url_prefix='/auth')
app.register_blueprint(supplier_bp, url_prefix='/supplier')

@jwt.unauthorized_loader
def token_ausente(err):
    return jsonify({'msg': 'Token não fornecido'}), 401

@jwt.invalid_token_loader
def token_invalido(err):
    return jsonify({'msg': 'Token inválido'}), 401

@jwt.expired_token_loader
def token_expirado(jwt_header, jwt_payload):
    return jsonify({'msg': 'Token expirado'}), 401


if __name__ == '__main__':
    app.run(debug=True)