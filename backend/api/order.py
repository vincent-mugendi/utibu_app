from flask import Blueprint, jsonify, request
from models.order import Order, db
from models.customer import Customer
from models.medication import Medication
from datetime import datetime

order_bp = Blueprint('order', __name__)

@order_bp.route('/order', methods=['POST'])
def place_order():
    data = request.json
    customer_id = data.get('customer_id')
    medication_id = data.get('medication_id')
    quantity = data.get('quantity')
    order_date = data.get('order_date')  # Get order date from request

    # Check if customer and medication exist
    customer = Customer.query.get(customer_id)
    medication = Medication.query.get(medication_id)

    if not customer:
        return jsonify({'error': 'Customer not found'}), 404
    if not medication:
        return jsonify({'error': 'Medication not found'}), 404

    # Check if there is enough stock
    if medication.stock_level < quantity:
        return jsonify({'error': 'Insufficient stock'}), 400

    # Create order
    new_order = Order(customer_id=customer_id, medication_id=medication_id, quantity=quantity, order_date=order_date)
    db.session.add(new_order)
    db.session.commit()

    return jsonify({'message': 'Order placed successfully'}), 201
