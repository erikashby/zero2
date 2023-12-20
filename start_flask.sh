#!/bin/bash
. development/bin/activate
export FLASK_APP=gpiotest.py
flask run --host=0.0.0.0
