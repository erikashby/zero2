import gpiozero, requests, json

import socket
testIP = "8.8.8.8"
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((testIP, 0))
myip = s.getsockname()[0]
s.close()

print(myip)

button = gpiozero.Button(2)
button_status = 0
last_button_status = 0



test_json = {"name":"test", "type":"button", "source ip":myip, "event":"toggle"}

while True:
    button_status = 0
    if button.is_pressed:
        button_status = 1
    #print(button_status)
    if button_status == 1 and last_button_status == 0:
        r = requests.put("http://192.168.1.166:5005/testput",json=test_json)
        print(r.status_code)
        last_button_status = 1
    if button_status == 0 and last_button_status == 1:
        last_button_status = 0