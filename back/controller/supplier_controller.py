from flask import Blueprint, request, jsonify
from models.supplier import Supplier
from flask_jwt_extended import jwt_required

supplier_bp = Blueprint('supplier', __name__)

@supplier_bp.route('/create', methods=['POST'])
@jwt_required()
def create_supplier():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    address = data.get('address')

    try:
        supplier = Supplier(name=name, email=email, phone=phone, address=address)
        supplier.save()

        return jsonify({'msg': 'Fornecedor cadastrado com sucesso'}), 200
    except Exception as e:
        print(e)
        return jsonify({'msg': 'Falha ao cadastrar fornecedor'}), 401

@supplier_bp.route('/findall', methods=['POST'])
@jwt_required()
def find_all_suppliers():
    try:
        suppliers = Supplier.select()
        suppliers_list = [s.__data__ for s in suppliers]
        
        return jsonify({'msg': 'Fornecedores carregados !', 'suppliers': suppliers_list})
    except Exception as e:
        print(e)
        return jsonify({'msg': 'Falha ao carregar fornecedores'}), 500
