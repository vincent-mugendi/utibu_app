import os
import sys
from flask_sqlalchemy import SQLAlchemy

# Add the path to the parent directory of the 'backend' directory to the Python path
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from app import app, db, Medication

# Push the application context
app.app_context().push()

def populate_medications():
    # Sample data for medications
    sample_medications = [
        {'medication_id': 1, 'name': 'HIV', 'description': 'Description A', 'stock_level': 100, 'price': 10.0},
        {'medication_id': 2, 'name': 'Diabetes', 'description': 'Description B', 'stock_level': 50, 'price': 20.0},
        {'medication_id': 3, 'name': 'Hypertension', 'description': 'Description C', 'stock_level': 46, 'price': 22.0},
        # Add more sample medication data here
        # Make sure to use unique medication_id values
    ]

    # Populate the medications table with sample data
    for medication_data in sample_medications:
        medication = Medication(**medication_data)
        db.session.add(medication)

    # Commit the changes to the database
    db.session.commit()

if __name__ == '__main__':
    populate_medications()
