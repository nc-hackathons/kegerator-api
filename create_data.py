from models import *
from sqlalchemy import *

session = db.session

# create batch
keg1 = Keg('left')
keg2 = Keg('right')

# create beer
beer1 = Beer('daisy cutter')
beer2 = Beer('budweiser')
beer3 = Beer('kirin')

# create batch
batch1 = Batch(beer1, keg1, 1)
batch2 = Batch(beer2, keg2, 1)
batch3 = Batch(beer3, keg1, 0)

# create pour
pour1 = Pour(batch1)

new_data = [keg1, keg2, beer1, beer2, beer3, batch1, batch2, batch3]

for data in new_data:
    session.merge(data)

session.commit()
