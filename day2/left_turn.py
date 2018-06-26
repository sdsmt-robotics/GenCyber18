#!/usr/bin/env python 

import geekbot
from time import sleep as wait

# This starts our robot up and connects to it
# syntax: robot_name = geekbot.Robot(baud_rate)
geek = geekbot.Robot(57600)
if geek.is_connected() == False:
    exit()

# Use the 'turn' function with a value between 0 and 100 for a left hand turn
# syntax: geek.turn_left( speed_to_turn )   
geek.turn_left(50)

# Use the 'wait' function to give the robot time to turn.
# This is the number you'll want to adjust to get 90 degree
# turns. Once you get 90 degree turns, write down the delay
# found!
# syntax: wait( number_of_seconds )
wait(2.9)

# Use the 'halt' function to stop the robot
geek.halt()
wait(.5)

# At the end of the script we shut the bot down
geek.shutdown()
