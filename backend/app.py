from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://vinnie:qwertyupi5@localhost/utibu_db'
db = SQLAlchemy(app)

# Define database models
class Customer(db.Model):
    __tablename__ = 'customers'
    customer_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    phone_number = db.Column(db.String(20))
    address = db.Column(db.String(255))

class Medication(db.Model):
    __tablename__ = 'medications'
    medication_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.Text)
    stock_level = db.Column(db.Integer)
    price = db.Column(db.Float)

class Order(db.Model):
    __tablename__ = 'orders'
    order_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.customer_id'))
    medication_id = db.Column(db.Integer, db.ForeignKey('medications.medication_id'))
    quantity = db.Column(db.Integer)
    order_date = db.Column(db.Date)
    status = db.Column(db.String(50))

    customer = db.relationship('Customer', backref='orders')
    medication = db.relationship('Medication', backref='orders')

# Add more models for other tables (Sales, Invoices, Payments, Statements, Inventory)

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

    # Create order
    new_order = Order(customer_id=customer_id, medication_id=medication_id, quantity=quantity)
    db.session.add(new_order)
    db.session.commit()

    return jsonify({'message': 'Order placed successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)
