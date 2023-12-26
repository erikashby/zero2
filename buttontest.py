from gpiozero import Button

button = Button(22)

button.wait_for_active()
print("Button 22 has been pressed.")