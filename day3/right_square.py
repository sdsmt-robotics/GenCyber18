#!/usr/bin/env python

import geekbot
from time import sleep as wait

geek = geekbot.Robot(57600)
if geek.is_connected() == False:
    exit()

sides_done = 0   # We've completed 0 of 4 sides
while sides_done < 4: # Until all sides are done, keep going!
    # Turn
    geek.turn_right(50, 2.5)  # Change the second number to get a 90 degree turn
                # speed, time


    # Drive forward
    geek.drive_forward(50, -15, 2.0)  # Change the second number to drive to robot straight
                 # speed, adjust, time

    # Stop
    wait(.5)

    # Another side done, increment our counter!
    sides_done += 1

geek.shutdown()
