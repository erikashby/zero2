import gpiozero, requests, json

button = gpiozero.Button(2)
button_status = 0
last_button_status = 0

test_json = {"name":"test", "event":"test event"}

while True:
    button_status = 0
    if button.is_pressed:
        button_status = 1
    #print(button_status)
    if button_status == 1 and last_button_status == 0:
        r = requests.put("http://192.168.1.166:5005/testput",json.JSONEncoder(test_json))
        print(r.status_code)
        last_button_status = 1
    if button_status == 0 and last_button_status == 1:
        last_button_status = 0