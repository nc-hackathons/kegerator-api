from flask import Flask
import api
import IPython
import os
import time
import math
import logging
import RPi.GPIO as GPIO
from Flow_Meter import *
app = Flask(__name__)

@app.route('/list')
def list_current_batches():
    return api.list_current_batches()

app.run()


KEG_PIN_1 = 4
GPIO.setmode(GPIO.BCM) # use real GPIO numbering
GPIO.setup(KEG_PIN_1,GPIO.IN, pull_up_down=GPIO.PUD_UP)

fm = Flow_Meter(1)
def doAClick(channel):
  currentTime = int(time.time() * 1000)
  if fm.enabled == True:
    fm.update(currentTime)

def sendData(flow_meter):
  flow_meter.getFormattedThisPour()
  flow_meter.fm_id

GPIO.add_event_detect(KEG_PIN_1, GPIO.RISING, callback=doAClick, bouncetime=20) # Beer, on Pin 23

while True:
  currentTime = int(time.time() * 1000)
  print fm.lastClick
  print fm.thisPour
  if (fm.thisPour > .01 and currentTime - fm.lastClick > 3000):
    print "Someone just poured " + fm.getFormattedThisPour() + " of beer from the keg"
    sendData(fm)
    fm.reset();
