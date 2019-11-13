# File: 06-triangle.py
# Author: David Lechner
# Date: 11/5/2019

'''How to draw a triangle with turtle graphics'''

import turtle

# The triangle has 3 sides. Each side of the triangle is 100 pixels long. Each
# corner has an interior angle of 60 degrees. We turn 120 degreed because that
# is the exterior angle.
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
