from db import db

class Medication(db.Model):
    __tablename__ = 'medications'
    medication_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.Text)
    stock_level = db.Column(db.Integer)
    price = db.Column(db.Float)

    def __repr__(self):
        return f"<Medication {self.medication_id}: {self.name}>"
