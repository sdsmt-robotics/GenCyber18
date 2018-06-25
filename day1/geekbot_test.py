#!/usr/bin/env python

import geekbot
import time

geek = geekbot.Robot(57600)
if geek.is_connected() == False:
    exit()

# Check lights
geek.lights_on()
time.sleep(.5)
geek.lights_off()

# Check IR servo and sensor
geek.set_ir_position(0)
time.sleep(.25)
print(geek.get_ir_distance())
time.sleep(.25)
geek.set_ir_position(90)
time.sleep(.25)
print(geek.get_ir_distance())
time.sleep(.25)
geek.set_ir_position(-90)
time.sleep(.25)
print(geek.get_ir_distance())
time.sleep(.25)
geek.set_ir_position(0)
time.sleep(.5)

# Check left wheel servo
geek.drive_left_wheel(90)
time.sleep(1)
geek.drive_left_wheel(-90)
time.sleep(1)
geek.drive_left_wheel(0)
time.sleep(.5)

# Check right wheel servo
geek.drive_right_wheel(90)
time.sleep(1)
geek.drive_right_wheel(-90)
time.sleep(1)
geek.drive_right_wheel(0)
time.sleep(.5)

#Check drive forward and halt
geek.drive_forward(80)
time.sleep(1)
geek.halt()



