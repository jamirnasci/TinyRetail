from flask import Blueprint, jsonify, url_for, redirect, request
from flask_jwt_extended import jwt_required

sales_bp = Blueprint('sales', __name__)

@sales_bp.route('/history', methods=['POST'])
@jwt_required()
def history():
    return jsonify({'msg': 'Sales'}), 200
