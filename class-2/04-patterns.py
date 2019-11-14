# file: 04-patterns.py
# author: David Lechner
# date: 11/07/2019

'''Learing how to draw geometric patterns using functions and loops'''

import turtle

def square(side):
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

turtle.speed(0)
for _ in range(12):
    square(200)
    turtle.left(360 / 12)  # We divide 360 degrees by 12 because we loop 12 times




