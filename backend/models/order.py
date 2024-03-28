from db import db

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

    def __repr__(self):
        return f"<Order {self.order_id}: Customer {self.customer_id} - Medication {self.medication_id}>"
