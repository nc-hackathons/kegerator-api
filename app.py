from flask import Flask
import api
import IPython
app = Flask(__name__)

@app.route('/list')
def list_current_batches():
    return api.list_current_batches()
    
app.run()
