import gpiozero, requests

button = gpiozero.Button(2)
button_status = 0
last_button_status = 0

while True:
    button_status = 0
    if button.is_pressed:
        button_status = 1
    #print(led)
    if button_status == 1 & last_button_status == 0:
        r = requests.get("http://192.168.1.204:5000/node/light?id=led0&action=on")
        print(r.status_code)
        last_button_status = 1
    if button_status == 0 & last_button_status == 1:
        r = requests.get("http://192.168.1.204:5000/node/light?id=led0&action=off")
        print(r.status_code)
        last_button_status = 0