from flask import Flask
import api
import IPython
app = Flask(__name__)

@app.route('/list')
def list_all_batches():
    return api.list_all_batches()
    
app.run()