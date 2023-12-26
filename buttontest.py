import gpiozero

button = gpiozero.Button(2)

while True:
    if button.is_pressed:
        print("Button is pressed")