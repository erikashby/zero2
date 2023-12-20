#Initial GPIO test app
#adding some more


from gpiozero import LED as GPIO
from flask import Flask
app = Flask(__name__)

led = GPIO(18)

@app.route('/')
def hello_world():
    return '200 OK - Hello ping !'


@app.route('/leave')
def good_bye():
    return '200 OK - good bye'

@app.route('/on')
def turn_led_on():
    led.on()
    return '200 OK - LED ON'

@app.route('/off')
def turn_led_off():
    led.off()
    return '200 OK - LED OFF'