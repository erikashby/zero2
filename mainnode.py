### This is the main code for a node in the system

import json
from gpiozero import LED as GPIO
from flask import Flask
app = Flask(__name__)
nodename = "node1"

led = GPIO(26)
led.on()

@app.route('/')
def status_res():
    status = {"NodeName":"node1", "Light":0}
    return status

@app.route('/node/status')
def status_result():
    status = {"NodeName":"node1", "Light":0}
    return status

#@app.route('/node/light')