#!/usr/bin/env python 

import geekbot
from time import sleep as wait

# This starts our robot up and connects to it
# syntax: robot_name = geekbot.Robot(baud_rate)
geek = geekbot.Robot(57600)
if geek.is_connected() == False:
    exit()

# This is our increment counter, a variable that stores the 
# number of times we have been through the loop below. It counts
# from 0-3.
i = 0

# This is the start of our 'while loop'. While i is less than 4, 
# it performs the actions between the hashtags below! Make sure 
# the indentation inside of the hashtags is one tab in
while i < 4:

##########################
# If the code finishes and the robot has returned to 
# its original position, you've made 4 90 degree turns!

    # Use the 'turn' function with a value between 0 and 100 for a right hand turn
    # syntax: geek.turn_right( speed_to_turn )   
    geek.turn_right(50)

    # Use the 'wait' function to give the robot time to turn.
    # This is the number you'll want to adjust to get 90 degree
    # turns. Once you get 90 degree turns, write down the delay
    # found!
    # syntax: wait( number_of_seconds )
    wait(2.9)

    # Use the 'halt' function to stop the robot
    geek.halt()
    wait(.5)

    # This increments our count in the 'i' variable every time 
    # we have turned. Once it gets to 4, our while loop exits!
    i += 1
##########################

# At the end of the script we shut the bot down
geek.shutdown()
