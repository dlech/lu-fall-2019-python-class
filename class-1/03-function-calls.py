# File: 03-function-calls.py
# Author: David Lechner
# Date: 11/5/2019

'''Learing about how to call a function.'''

'''
In coding, functions can be like mathematical functions that perform an
operation on a value. They can also tell the program to do something, like
draw on the screen.

Functions have a name, parentheses and arguments.

    name(arguments)

The name can be name (Python naming rules are that it has to start with a letter
and only contain a-z, A-Z, 0-9 and _ and is case-sensitive).

The parentheses are important - they are what tells Python to "call" the
function (call means make it do something).

The function may have one or more arguments that act as inputs to the function
and change how the function behaves.
'''

import turtle

# This calls the "forward()" function in the "turtle" module. It tells the
# turtle to move forward for 100 pixels on the screen.
turtle.forward(100)

# This function takes two arguments, an X and Y coordinate.
turtle.goto(100, 100)
