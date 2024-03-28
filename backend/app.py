from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Instance of the Flask class
app = Flask(__name__)

# Configuration for the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://localhost/utibu_db?driver=ODBC+Driver+17+for+SQL+Server'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy extension
db = SQLAlchemy(app)

@app.route('/order', methods=['POST'])
def handle_order():
    data = request.get_json()
    customer_id = data.get('customer_id')
    medication_id = data.get('mediaction_id')
    quantity = data.get('quantity')

    success, message = place_order(customer_id, medication_id, quantity)

    if success:
        return jsonify({'message': message}), 201
    else:
        return jsonify({'message': message}), 400

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
