import gpiozero, requests, json, socket
from datetime import datetime


### Get IP
testIP = "8.8.8.8"
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((testIP, 0))
myip = s.getsockname()[0]
s.close()
### Get IP

button = gpiozero.Button(2)
button_status = 0
last_button_status = 0



test_json = {"name":"test", 
             "type":"node", 
             "version":"0.1",
             "source ip":myip
             }

while True:
    button_status = 0
    if button.is_pressed:
        button_status = 1
        # get the current time
        now = datetime.now()
        # mm/dd/YY H:M:S
        now = now.strftime("%m/%d/%Y %H:%M:%S")
    
    if button_status == 1 and last_button_status == 0:
        test_json["event"] = {
            "datetime":now,
            "type":"button",
            "ID":"btn0",
            "event":"button_pressed"
        }

        status_url = "http://" + myip + ":5000/node/status"
        status = requests.get(status_url).json()

        test_json["status"] = status['status']

        print(test_json)

        r = requests.put("http://192.168.1.166:5005/testprint",json=test_json)
        print(r.status_code)
        last_button_status = 1
    if button_status == 0 and last_button_status == 1:
        last_button_status = 0