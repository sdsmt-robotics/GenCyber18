#!/usr/bin/env python

import geekbot
from time import sleep as wait

geek = geekbot.Robot(57600)
if geek.is_connected() == False:
    exit()

###########################

# Negative = to turn more right
# Positive = turn more left
# syntax: geek.drive_forward( speed, right_wheel_adjustment, seconds to drive before stopping )
geek.drive_forward(70, 0, 2.0)

# Use the 'halt' function to stop your robot
geek.halt()

###########################

# This shuts down the robot and closes the USB connection
geek.shutdown()
