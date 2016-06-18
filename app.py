from flask import Flask
from models import *
import IPython
app = Flask(__name__)

@app.route('/batches', methods=['GET'])
def hello_world():
    return Batch.query.all()
    
app.run()
