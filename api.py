from models import *

def list_all_batches:
    

def create_batch(beer_name, keg_name):
    beer = db.session.query(Beer).filter_by(name=beer_name).first()
    keg = db.session.query(Keg).filter_by(name=keg_name).first()
    db.session.merge(Batch(beer, keg, True))
    db.session.commit

def create_beer(beer_name):

