from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql:/nc:kegerator1234@127.0.0.1:8080/kegerator'
db = SQLAlchemy(app)

class Batch(db.Model):
    __tablename__ = 'batches'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)
    current = db.Column(db.Boolean)
    beer_id = db.Column(db.Integer, db.ForeignKey('beers.id'))
    keg_id = db.Column(db.Integer, db.ForeignKey('kegs.id'))
    
    def __init__(self, beer, keg, current):
        self.current = current
        self.beer_id = beer.id
        self.keg_id = keg.id
        self.timestamp = datetime.utcnow()

class Beer(db.Model):
    __tablename__ = 'beers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    batches = db.relationship('Batch', backref='beer', lazy='dynamic')
    
    def __init__(self, name):
        self.name = name
    
class Keg(db.Model):
    __tablename__ = 'kegs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    batches = db.relationship('Batch', backref='keg', lazy='dynamic')
    
    def __init__(self, name):
        self.name = name
    
class Pour(db.Model):
    __tablename__ = 'pours'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)
    batch_id = db.Column(db.Integer, db.ForeignKey('batches.id'))
    
    def __init__(self, batch):
        self.batch_id = batch.id
        self.timestamp = datetime.utcnow()

