#!/usr/bin/env python

import geekbot
from time import sleep as wait

geek = geekbot.Robot(57600)
if geek.is_connected() == False:
    exit()

#####################################

MIN_DIST = 15 # Change this number to detect closer ojbects 

while 1:
    
    front_dist = geek.get_ir_distance() 
    print(front_dist)

    if front_dist <= MIN_DIST:
            geek.lights_on()
            geek.beep(1)
            geek.lights_off()
            geek.set_ir_position(0)
            wait(.5)               
            left_dist = geek.get_ir_distance()

            if left_dist <= MIN_DIST:
                geek.lights_on()
                geek.beep(1)
                geek.lights_off()
                geek.set_ir_position(90)    
                geek.turn_right(50, 0.75)   # Change the speed and time to turn 90* 
                                        
            else:
                geek.set_ir_position(90)
                geek.turn_left(50, 0.75)    # Change the speed and time to turn 90* 
    wait(.2)

##################################
geek.shutdown()

