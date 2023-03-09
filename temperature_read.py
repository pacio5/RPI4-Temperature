import LM75
from gpiozero import LED
import time

led_blue = LED(17)
led_red = LED(22)

sensor = LM75.LM75()

while(True):
    temp = sensor.getTemp()

    print(temp)
    if temp > 20:
        led_red.on()
        led_blue.off()
    else: 
        led_red.off()
        led_blue.on()
    
    time.sleep(1)
