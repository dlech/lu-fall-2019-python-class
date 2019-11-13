# File: 07-circle.py
# Author: David Lechner
# Date: 11/5/2019

'''How to draw a circle with turtle graphics'''

import turtle

# There is a special function to draw a circle. The argument is the radius
# of the circle, so this circle will have diameter of 100 pixles.
turtle.circle(50)

# When we have two arguments, the second one tells it the angle of the arc
# to draw. 360 degrees is a full circle, so this draws 1/2 of a circle
turtle.circle(100, 180)

# When we have three arguments, the 3rd one tells how many segments to use
# to draw the circle. If we use a small number, then it will no longer look
# like a circle! This has 4 steps, so it makes a square.
turtle.circle(50, 360, 4)
