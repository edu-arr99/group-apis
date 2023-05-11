from flask import Flask
from flask import request, jsonify
from flask_mongoengine import MongoEngine

app = Flask(__name__)

@app.route('/group01')
def group01():
    return jsonify({'result': 'este es el grupo 01'})

@app.route('/group02')
def group01():
    return jsonify({'result': 'este es el grupo 02'})

@app.route('/group03')
def group01():
    return jsonify({'result': 'este es el grupo 03'})

@app.route('/group01')
def group01():
    return jsonify({'result': 'este es el grupo 04'})

if __name__ == "__main__":
    app.run(debug=True, port=5000)

# readme 
# pip install flask
