#!flask/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 16:04:40 2019
@author: pk
"""

from flask import Flask,json,request,jsonify
from main import start

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['POST'])
def predict():
    sitename = request.json['sitename']
    start(sitename)
    return json.dumps({'message' : 'The file is being made. Please wait'}), 200, {'Content-Type': 'application/json'}

if __name__ == '__main__':
    app.run(debug=True)
