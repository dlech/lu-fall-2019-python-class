# file: 02-functions.py
# author: David Lechner
# date: 11/07/2019

'''Learing how to define our own functions.'''

import turtle

# LEARN: The "def" keyword is short for "define". We use it to define our own
# functions.

# LEARN: Like loops, we have a line that ends with a ":". Everything after that
# gets indented 4 spaces to make a block of code.

# LEARN: The block of code in the function does not run when we define it. We
# have to "call" the function later!


def triangle():
    for _ in range(3):
        turtle.forward(100)
        turtle.left(120)

def square():
    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)

# We call our own functions the same why we have been calling the turtle
# functions - by writing the name with parentheses after it.
triangle()
square()

# We want to use functions because it lets us reuse the same code without having
# to copy it. For example, if we want to draw another square, we can do this:

turtle.penup()
turtle.backward(200)
turtle.pendown()
square()
