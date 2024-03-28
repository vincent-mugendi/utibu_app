from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Instance of the Flask class
app = Flask(__name__)

# Configuration for the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://localhost/utibu_db?driver=ODBC+Driver+17+for+SQL+Server'

# Initialize the SQLAlchemy extension
db = SQLAlchemy(app)

# A simple model for testing
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

# Route for the root URL ('/')
@app.route('/')
def hello_world():
    """
    A simple route that returns a 'Hello, World!' message.
    """
    return 'Hello, World!'

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
