from flask import Blueprint, request, jsonify
from models.product import Product
from flask_jwt_extended import jwt_required

product_bp = Blueprint('products', __name__)

@product_bp.route('/create', methods=['POST'])
@jwt_required()
def create_product():
    data = request.get_json()
    name = data.get('name')
    buy_price = data.get('buy_price')
    sell_price = data.get('sell_price')
    quantity = data.get('quantity')
    supplier = data.get('supplier')

    try:
        product = Product(name=name, buy_price=buy_price, sell_price=sell_price, quantity=quantity, supplier=supplier)
        product.save()
        return jsonify({'msg': 'Produto cadastrado com sucesso'}), 200
    except Exception as e:
        print(e)
        return jsonify({'msg': 'Falha ao cadastrar produto'}), 500

