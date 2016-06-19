from flask import Flask
import api
import IPython
import os
import time
import math
import logging
app = Flask(__name__)
CORS(app)

@app.route('/batches')
def list_current_batches():
    return api.list_current_batches()

@app.route('/')
def list_all_batches():
	return api.list_all_batches()

@app.route('/kegs')
def list_kegs():
	return api.list_kegs()

@app.route('/create_batch', methods=['POST'])
def create_batch():
	return api.create_batch(request.form['beer_name'], request.form['keg_name'])
    
app.run(host='0.0.0.0')
