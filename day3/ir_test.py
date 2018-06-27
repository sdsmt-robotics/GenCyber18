#!/usr/bin/env python

import geekbot
from time import sleep as wait

geek = geekbot.Robot(57600)
if geek.is_connected() == False:
    exit()

#####################################

MIN_DIST = 20 # Change this number to detect closer ojbects 

while 1:
    
    front_dist = geek.get_ir_distance() # front_dist now holds # of cm to object 

    if dist <= MIN_DIST:
        print("I see something at: " + str(front_dist) + " cm")
        geek.lights_on()
        geek.beep(1)
        geek.lights_off()
    
    wait(.2)

##################################
geek.shutdown()

