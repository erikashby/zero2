import gpiozero

button = gpiozero.Button(2)

while True:
    print("waiting for button")
    if button.is_pressed:
        print("Button is pressed")
        