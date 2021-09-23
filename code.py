from adafruit_circuitplayground import cp
from time import sleep

color = (0,0,0)

while True:
    cp.pixels.brightness = cp.light * .01
    if cp.button_a:
        color = (255, 0, 0)
    elif cp.button_b:
        color = (0, 255, 0)

    cp.pixels.fill(color)