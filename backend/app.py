from flask import Flask

# instance of the Flask class
app = Flask(__name__)

# route for the root URL ('/')
@app.route('/')
def hello_world():
    """
    A simple route that returns a 'Hello, World!' message.
    """
    return 'Hello, World!'

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
