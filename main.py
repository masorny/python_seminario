#!/usr/bin/env python3
from flask import Flask, Blueprint
from login import login

app = Flask(__name__)

# Servicio rest
app.register_blueprint(login)

@app.route('/', methods=['GET'])
def hello():
    return 'Hola mundo'

if __name__ == "__main__":
    app.run(
            host="0.0.0.0", 
            port=5000,
            debug=True
            )