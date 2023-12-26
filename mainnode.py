### This is the main code for a node in the system

import json
from datetime import datetime
from gpiozero import LED as GPIO
from flask import Flask, request
app = Flask(__name__)

# Server sets the var's value
nodename = "node1"
leds = [GPIO(12),GPIO(27),GPIO(22),GPIO(6),GPIO(25)]

light_status = [{'id':'led0', 'state':leds[0].value},
                {'id':'led1', 'state':leds[1].value},
                {'id':'led2', 'state':leds[2].value},
                {'id':'led3', 'state':leds[3].value},
                {'id':'led4', 'state':leds[4].value}]

status_led = GPIO(26)
status_led.on()

@app.route('/')
def status_home():
    status = get_status()
    return status

@app.route('/node/status')
def status_res():
    status = get_status()
    return status

@app.route('/node/light')
def change_light():
    id = int(request.args.get('id'))
    action = request.args.get('action')
    if action == "on":
        light_on(id)
    else:
        light_off(id)
    return "Status light is " + light_status[id]

# Button pressed
# send to server


# Change lights status
def light_on(_id):
    leds[_id].on()

def light_off(_id):
    leds[_id].off()

def update_light_status():
    light_status = [{'id':'led0', 'state':leds[0].value},
                {'id':'led1', 'state':leds[1].value},
                {'id':'led2', 'state':leds[2].value},
                {'id':'led3', 'state':leds[3].value},
                {'id':'led4', 'state':leds[4].value}]
    
    return light_status

# def status, ask the pi to return current status on the machine.
def get_status():
    # get the current time
    now = datetime.now()
    # dd/mm/YY H:M:S
    now = now.strftime("%m/%d/%Y %H:%M:%S")

    # build the json file status
    curr_status = {'nodeName':nodename,
              'status': {
                  'dateTime' : now,
                  'light_status' : update_light_status()
              }
              }
    
    return curr_status