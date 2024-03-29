from flask import Blueprint, jsonify, request
from models.statement import Statement
from db import db

statement_bp = Blueprint('statement', __name__)

@statement_bp.route('/statement/<int:customer_id>', methods=['GET'])
def get_statements(customer_id):
    statements = Statement.query.filter_by(customer_id=customer_id).all()
    return jsonify([statement.serialize() for statement in statements])

@statement_bp.route('/statement/<int:customer_id>', methods=['POST'])
def create_statement(customer_id):
    data = request.json
    statement_date = data.get('statement_date')
    balance = data.get('balance')

    new_statement = Statement(customer_id=customer_id, statement_date=statement_date, balance=balance)
    db.session.add(new_statement)
    db.session.commit()

    return jsonify({'message': 'Statement created successfully'}), 201
