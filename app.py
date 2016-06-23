from flask import Flask, request
import api
import IPython
import os
import time
import math
import logging
from flask.ext.cors import CORS
from flask_socketio import SocketIO
from models import *
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
	print "CHANGING..."
	print request.json
	print request.json['tap_position']
	keg_id = request.json['keg']

        print "WTF????"
	all_pours = Pour.query.filter_by(batch_id=4).all()
	print len(all_pours)
	

	current_batch = Batch.query.filter_by(current=True, keg_id=keg_id).first()
	if request.json['tap_position'] == "OFF":
		pour_activity = Pour(current_batch, request.json['amount_poured'])
		db.session.add(pour_activity)
		db.session.commit() # Adds pour to database
	socketio.emit('pour_event', { 'keg': keg_id, 'tap_position': request.json['tap_position'] })
	return ''

#app.run(host='0.0.0.0')
socketio.run(app, host='0.0.0.0', debug=True)
