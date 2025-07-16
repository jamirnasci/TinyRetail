from flask import Blueprint, jsonify, url_for, redirect, request
from flask_jwt_extended import jwt_required
from models.sale import Sale
from models.sale_list import SaleList

sales_bp = Blueprint('sales', __name__)

@sales_bp.route('/create', methods=['POST'])
def create_sale():
    data = request.get_json()
    total = data.get('total')
    tt_itens = data.get('total_itens')
    s_list = data.get('list')

    try:
        sale = Sale(total=total, total_itens=tt_itens)
        sale.save()
        for p in s_list:
            tt = p.get('total_item')
            product_id = p.get('id')
            item = SaleList(total_item=tt, product=product_id, sale=sale.id)
            item.save()
        return jsonify({'msg': 'Venda cadastrada com sucesso'}), 200
    except Exception as e:
        print(e)
        return jsonify({'msg': 'Falha ao cadastrar venda'}), 500

@sales_bp.route('/history', methods=['POST'])
@jwt_required()
def history():
    try:
        sales = Sale.select()
        sales_list = [s.__data__ for s in sales]
        print('ok')
        return jsonify({'msg': 'Vendas carregadas com sucesso', 'history': sales_list})
    except Exception as e:
        return jsonify({'msg': 'Falha ao carregar vendas'}), 500
        print(e)