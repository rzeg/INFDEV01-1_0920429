﻿from Start import *

#For this assigment you are asked to use the drawing facilities of python provided by the turtle library.
#For simplicity we provide you an interfae that hides the complexitie of the turtule library.
#It is important for the correct execution of this program that you do not remove the header and the footer of
# this file.
#Add your code within the def Program(): ... (mind the spaces)
#
#If you try to run this sample a white screen will appear and a black triangle (from now on pen) will be drawn 
# in the middle.
#To move the pen we provide you two instructions: 
#   (i)    forward (amount)           'forward' moves the pen by 'amount' steps
#                                     amount is a value of type Integer
#
#   (ii)   turn (amount)              'turn' rotates the pen by 'amount' degrees
#                                     amount is a value of type Integer
#
#   (iii)  change_color_to (color)    'change_color_to' changes the color of the pen into 'color'
#                                      the possible colors are: Black, Green, Blue, and Red
#
#By combining forward and turn (inside loops) you are able to draw lots of nice shapes :) good luck and have fun!


def Program():
    #SUPPORTING INSTRUCTION
    #use 'get()' to read the input and store it into a variable. The input is provided in the shape of an ASCII integer number.
    #Check https://en.wikipedia.org/wiki/ASCII for the complete ASCII table 
    #Example:
    # The following code reads the input and stores it into a variable called 'x'. 'x' is then printed out into the console
    # x =get()
    # print (x)
    


    #---------------------------------------------------------------------
    #                  PUT YOUR CODE BELOW
    #---------------------------------------------------------------------

    input = get()
    if(input == 119):
        forward(3)

    elif(input == 97):
        turn(-15)
    elif(input == 100):
        turn(15)
    print(input)

    if(input == 13):
        DrawColourfulPyramid()

def DrawColourfulPyramid():
    for y in range(0,100):
        if(y % 2 == 0):
            change_color_to(Red)
        elif(y % 5 == 0):
            change_color_to(Green)
        else:
            change_color_to(Black)
        turn(90)
        forward(y)

run(Program)
from End import *
