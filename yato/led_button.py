
from gpiozero import LED
from gpiozero import Button


led = LED(4)
button = Button(21)


while True:
    if button.is_pressed:
        led.on()
    else:
        led.off()
