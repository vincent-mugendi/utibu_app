# populate_customers.py

import os
import sys
from flask_sqlalchemy import SQLAlchemy

# Add the path to the parent directory of the 'backend' directory to the Python path
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from app import app, db, Customer

# Push the application context
app.app_context().push()

def populate_customers():
    # Sample data for 10 customers
    sample_customers = [
        {'customer_id': 1, 'name': 'John Doe', 'email': 'john.doe@example.com', 'phone_number': '1234567890', 'address': '123 Main St'},
        {'customer_id': 2, 'name': 'Jane Smith', 'email': 'jane.smith@example.com', 'phone_number': '0987654321', 'address': '456 Elm St'},
        # Add more sample customer data here
        # Make sure to use unique customer_id values
    ]

    # Populate the customers table with sample data
    for customer_data in sample_customers:
        customer = Customer(**customer_data)
        db.session.add(customer)

    # Commit the changes to the database
    db.session.commit()

if __name__ == '__main__':
    populate_customers()
