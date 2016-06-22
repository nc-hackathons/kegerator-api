from flask import Flask, request
import api
import IPython
import os
import time
import math
import logging
from flask.ext.cors import CORS
from flask_socketio import SocketIO
app = Flask(__name__)
socketio = SocketIO(app)
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
    
@app.route('/pour_event', methods=['POST'])
def pour_event():
	socketio.emit('pour_event', { 'keg': request.json['keg'], 'tap_position': request.json['tap_position'] })
	return ''

#app.run(host='0.0.0.0')
socketio.run(app, host='0.0.0.0', debug=True)
