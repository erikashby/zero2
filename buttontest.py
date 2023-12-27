import gpiozero

button = gpiozero.Button(2)
led = 0

while True:
    led = 0
    if button.is_pressed:
        led = 1
    print("led")
        