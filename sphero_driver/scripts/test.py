#!/usr/bin/python

from sphero_driver import sphero_driver
from time import sleep

# if you know your Sphero's address
# sphero = sphero_driver.Sphero("Sphero", "FF:CD:AA:99:45:00")
sphero = sphero_driver.Sphero()

while not sphero.is_connected:
    sphero.connect()

sleep(1)
sphero.set_rgb_led(255, 0, 0, 0, False)
sleep(1)
sphero.set_rgb_led(0, 255, 0, 0, False)
sleep(1)
sphero.set_rgb_led(0, 0, 255, 0, False)
sleep(1)
