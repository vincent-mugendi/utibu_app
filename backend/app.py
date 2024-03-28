from flask import Flask, request, jsonify
from db import db
from models.customer import Customer
from models.medication import Medication
from models.order import Order

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://vinnie:qwertyupi5@localhost/utibu_db'

db.init_app(app)


# Endpoint to place an order
# Endpoint to place an order
@app.route('/order', methods=['POST'])
def place_order():
    data = request.json
    customer_id = data.get('customer_id')
    medication_id = data.get('medication_id')
    quantity = data.get('quantity')

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

    # Update stock level
    medication.stock_level -= quantity

    # Create order
    new_order = Order(customer_id=customer_id, medication_id=medication_id, quantity=quantity)
    db.session.add(new_order)
    db.session.commit()

    return jsonify({'message': 'Order placed successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)
