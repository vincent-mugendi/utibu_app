from flask import Flask
from db import db
from api.order import order_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://vinnie:qwertyupi5@localhost/utibu_db'

db.init_app(app)

app.register_blueprint(order_bp)

if __name__ == '__main__':
    app.run(debug=True)
