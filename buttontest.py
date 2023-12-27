import gpiozero, requests

button = gpiozero.Button(2)
led = 0

while True:
    led = 0
    if button.is_pressed:
        led = 1
    #print(led)
    if led == 1:
        r = requests.get("http://192.168.1.204:5000/node/light?id=led0&action=on")
        print(r.status_code)
    else:
        r = requests.get("http://192.168.1.204:5000/node/light?id=led0&action=off")
        print(r.status_code)