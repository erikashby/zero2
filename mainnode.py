### This is the main code for a node in the system

import json
from gpiozero import LED as GPIO
from flask import Flask, request
app = Flask(__name__)

# Server sets the var's value
nodename = "node1"
light_status = [0,0,0,0,0]


leds = [GPIO(12),GPIO(27),GPIO(22),GPIO(6),GPIO(25)]

status_led = GPIO(26)
status_led.on()

@app.route('/')
def status_res():
    status = {"NodeName":nodename, "Lights":light_status}
    return status

@app.route('/node/status')
def status_result():
    status = {"NodeName":nodename, "Light":light_status}
    return status

@app.route('/node/light')
def change_light():
    id = request.args.get('id')
    action = request.args.get('action')
    if action == "on":
        light_on(id)
    else:
        light_off(id)

# Button pressed
# send to server


# Change lights status
def light_on(_id):
    light_status[_id] = 1
    leds[_id].on()

def light_off(_id):
    light_status[_id] = 0
    leds[_id].off()

def light_toggle(_id):
    light_status[_id] = (light_status[_id] + 1) % 2 
    leds[_id].toggle()