from models import *
import json

def list_current_batches():
    result = []
    current_batches = db.session.query(Batch).filter_by(current=True).all()
    return json.dumps([batch.to_json() for batch in current_batches])

def list_all_batches():
    result = []
    batches = db.session.query(Batch).all()
    return json.dumps([batch.to_json() for batch in batches])

def list_kegs():
    result = []
    for keg in db.session.query(Keg).all():
        keg_dict = keg.to_json()
        keg_dict["batch"] = db.session.query(Batch).filter_by(keg=keg,current=True).first().to_json()
        result.append(keg_dict)
    return json.dumps(result)

def create_batch(beer_name, keg_name):
    beer = Beer.query.filter_by(name=beer_name).first()
    keg = Keg.query.filter_by(name=keg_name).first()
    old_batch = Batch.query.filter_by(keg_id=keg.id).first()
    old_batch.current = False
    db.session.merge(Batch(beer, keg, True))
    db.session.commit()
    

