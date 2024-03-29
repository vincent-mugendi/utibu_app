from flask import Flask
from db import db
from api.order import order_bp
from api.statement import statement_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://vinnie:qwertyupi5@localhost/utibu_db'

db.init_app(app)

app.register_blueprint(order_bp)
app.register_blueprint(statement_bp)

if __name__ == '__main__':
    app.run(debug=True)
