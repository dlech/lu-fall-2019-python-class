# File: 03-graph_calc.py
# Author: David Lechner
# Date: 11/12/2019

'''A graphing calculator using turtle graphics'''

import turtle


def draw_x_axis():
    '''This draws the horizontal X axis with an arrow on each end.'''
    # LEARN: the tracer() function turns the animation on or off. True and False
    # are Python keywords. True means "on" and False means "off".

    # Turn animation off so drawing is much faster
    turtle.tracer(False)
    turtle.penup()
    turtle.goto(-200, 0)
    turtle.shape('arrow')
    turtle.setheading(180)
    turtle.stamp()
    turtle.pendown()
    turtle.goto(200, 0)
    turtle.setheading(0)
    turtle.stamp()
    # turn animation back on so that the screen is updated with everything above
    turtle.tracer(True)



def draw_y_axis():
    '''This draws the vertical Y axis with an arrow on each end.'''
    turtle.tracer(False)
    turtle.penup()
    turtle.goto(0, -200)
    turtle.shape('arrow')
    turtle.setheading(270)
    turtle.stamp()
    turtle.pendown()
    turtle.goto(0, 200)
    turtle.setheading(90)
    turtle.stamp()
    turtle.tracer(True)


def graph():
    '''This plots the mathematical function y = 0.5 * x + 50'''
    turtle.penup()
    turtle.hideturtle()
    turtle.speed(0)
    turtle.pencolor('blue')
    turtle.pensize(3)
    for x in range(-200, 200):
        y = 0.5 * x + 50
        turtle.goto(x, y)
        turtle.pendown()

# don't forget to call the functions after we define them!
draw_x_axis()
draw_y_axis()
graph()
