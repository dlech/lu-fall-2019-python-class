# file: 03-arguments.py
# author: David Lechner
# date: 11/07/2019

'''Learing how to add arguments to functions'''

import turtle

# LEARN: Arguments are the things inside of the parentheses of a function. Kind
# of like in math class where we have a function f(x). "x" is the "argument".
# It is just a name that represents a value.

# Before, the length of each side was always 100. We can use an argument instead
# that allows us to use the same function to make a shape with any size.

def triangle(side):  # we added "side" in this line
    for _ in range(3):
        turtle.forward(side)  # we changed "100" to "size" in this line
        turtle.left(120)


# Now, when we call the function, we have to give a value for the argument,
# otherwise we will get an error.

triangle(100)  # this draws the same size triangle as before


# But now we can draw shapes with other sizes too

triangle(200)
triangle(300)
