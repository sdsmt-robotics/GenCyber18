#!/usr/bin/env python

import geekbot
from time import sleep as wait

# This starts our robot up and connects to it
# syntax: robot_name = geekbot.Robot( "serial_port_location", baud_rate)
geek = geekbot.Robot(57600)
if geek.is_connected() == False:
    exit()

###########################

# Here, use the 'drive_forward' function and change the 'adjust'
# parameter (the second one!) so your robot drives straight. Once
# the robot drives straight, write down the adjustment (and speed) 
# you used down! Every speed will need a different adjustment

# Negative = to turn more right
# Positive = turn more left
# syntax: geek.drive_forward( speed, right_wheel_adjustment )
# syntax: geek.drive_backward( speed, right_wheel_adjustment )
geek.drive_forward(50, -15)

# Use the 'wait' function to let the geekbot drive for a while
# syntax: wait( number_of_seconds )
wait(2.0)

# Use the 'halt' function to stop your robot
geek.halt()

###########################

# This shuts down the robot and closes the USB connection
geek.shutdown()
