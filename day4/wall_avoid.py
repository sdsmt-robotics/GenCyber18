#! /usr/bin/env python

import geekbot
import sys
from time import sleep as wait

geek = geekbot.Robot(57600)
if geek.is_connected() == False:
    exit()

MIN_DIST = 11

while 1:
    # Get front distance

    # If there's a wall in front

        # Stop the robot

        # Beep and flash lights

        # Get left distance

        # If there's a wall to the left

            # Beep and flash lights

            # Turn right

        # Else, there's not a wall to the left

            # Turn left

    # Else, there's not a wall in front

        # Drive forward

    wait(.2)
    
    ##### IGNORE THIS PLEASE #####
    except KeyboardInterrupt:
        geek.shutdown()
        break
