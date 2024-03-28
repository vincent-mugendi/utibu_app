from models.medication import Medication
from models.order import Order
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def place_order(customer_id, medication_id, quantity):
    medication = Medication.query.get(medication_id)
    if not medication:
        return False, 'Medication not found'
    
    if medication.stock < quantity:
        return False, 'Not enough stock'

    medication.stock -= quantity
    db.session.commit()

    order = Order(customer_id=customer_id, medication_id=medication_id, quantity=quantity)
    db.session.add(order)
    db.session.commit()

    return True, 'Order placed successfully'
