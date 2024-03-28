from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Medication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    stock_level = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Medication {self.name}>"
