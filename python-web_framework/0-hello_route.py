#!/usr/bin/python3
from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route for the root URL with strict_slashes=False
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

if __name__ == '__main__':
    # Run the Flask app on 0.0.0.0 and port 5000
    app.run(host='0.0.0.0', port=5000)
