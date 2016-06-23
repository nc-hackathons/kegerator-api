from models import *
import json

def list_current_batches():
    result = []
    db.session.query(Batch)
    current_batches = db.session.query(Batch).filter_by(current=True).all()
    return json.dumps([batch.to_json() for batch in current_batches])

def list_all_batches():
    result = []
    current_batches = db.session.query(Batch).all()
    return json.dumps([batch.to_json() for batch in current_batches])

    
def list_kegs():
    result = []
    for keg in Keg.query.all():
        keg_dict = keg.to_json()
        keg_dict["batch"] = db.session.query(Batch).filter_by(keg=keg).order_by('-id').first().to_json()
	print "POUR COUNT FOR BATCH"
	print len(db.session.query(Pour).filter_by(batch_id=4).all())
	print "LITERALLY WHAT I'M RETURNING"
	
        result.append(keg_dict)
    return json.dumps(result)

def create_batch(beer_name, keg_name):
    beer = Beer.query.filter_by(name=beer_name).first()
    keg = Keg.query.filter_by(name=keg_name).first()
    old_batch = Batch.query.filter_by(keg_id=keg.id).first()
    old_batch.current = False
    db.session.merge(Batch(beer, keg, True))
    db.session.commit()
    

