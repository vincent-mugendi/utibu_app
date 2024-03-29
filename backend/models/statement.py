from db import db

class Statement(db.Model):
    __tablename__ = 'statements'
    statement_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.customer_id'))
    statement_date = db.Column(db.Date)
    balance = db.Column(db.Float)

    def __init__(self, customer_id, statement_date, balance):
        self.customer_id = customer_id
        self.statement_date = statement_date
        self.balance = balance