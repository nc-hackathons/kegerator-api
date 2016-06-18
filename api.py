from models import *
import json

def list_current_batches():
    result = []
    current_batches = Batch.query.filter_by(current=True).all()
    return json.dumps([batch.to_json() for batch in current_batches])

def list_all_batches():
    result = []
    current_batches = Batch.query.all()
    return json.dumps([batch.to_json() for batch in current_batches])

    
def list_kegs():
    result = []
    for keg in Keg.query.all():
        keg_dict = keg.to_json()
        keg_dict["batch"] = Batch.query.filter_by(keg=keg).first().to_json()
        result.append(keg_dict)
    return json.dumps(result)

def create_batch(beer_name, keg_name):
    beer = Beer.query.filter_by(name=beer_name).first()
    keg = Keg.query.filter_by(name=keg_name).first()
    db.session.merge(Batch(beer, keg, True))
    db.session.commit()
    

