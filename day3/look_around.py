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
        beep(1)

        geek.set_ir_position(0) # Look Left!
        wait(.2)                # Wait for robot to look left
        left_dist = geek.get_ir_distance()
        print("Left: " + str(left_dist) + " cm")
        
        geek.set_ir_position(0) # Look right!
        wait(.5)                # Wait for robot to look right
        right_dist = geek.get_ir_distance()
        print("Right: " + str(right_dist) + " cm")
    
    wait(.2)

##################################
geek.shutdown()

