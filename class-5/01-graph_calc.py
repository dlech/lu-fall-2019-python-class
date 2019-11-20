# File: graph_calc.py
# Author: David Lechner
# Date: 11/19/2019

'''A graphing calculator using turtle graphics'''

import turtle

# Adjust these values to change the viewable window of the plot
X_MIN = -40
X_MAX = 40
X_GRID_LINE = 10
Y_MIN = -50
Y_MAX = 50
Y_GRID_LINE = 10

# We moved the math functions to the top of the program so they are easy to
# change. We also now have two functions that we will graph.

def func1(x):
    return x


def func2(x):
    return -x + 10


def draw_x_tick(x):
    '''This draws a tick mark on the X axis

    Parameters
    ----------
    x : integer
        The position on the X axis where the tick mark should be drawn
    '''
    turtle.penup()
    turtle.goto(x, 0)
    turtle.setheading(90)
    d = (Y_MAX - Y_MIN) * 0.02
    turtle.pendown()
    turtle.forward(d)
    turtle.backward(2 * d)


def draw_y_tick(y):
    '''This draws a tick mark on the Y axis

    Parameters
    ----------
    y : integer
        The position on the Y axis where the tick mark should be drawn
    '''
    turtle.penup()
    turtle.goto(0, y)
    turtle.setheading(0)
    d = (X_MAX - X_MIN) * 0.02
    turtle.pendown()
    turtle.forward(d)
    turtle.backward(2 * d)


def draw_x_axis():
    '''This draws the horizontal X axis'''
    turtle.tracer(False)
    turtle.penup()
    turtle.goto(X_MIN, 0)
    turtle.shape('arrow')
    turtle.setheading(180)
    turtle.stamp()
    turtle.write('  ' + str(X_MIN))
    turtle.pendown()
    turtle.goto(X_MAX, 0)
    turtle.setheading(0)
    turtle.stamp()
    turtle.write('   ' + str(X_MAX))
    steps = (X_MAX - X_MIN) // X_GRID_LINE
    for x in range(X_MIN, X_MAX, steps):
        if x == X_MIN:
            continue
        draw_x_tick(x)
    turtle.tracer(True)


def draw_y_axis():
    '''This draws the horizontal Y axis'''
    turtle.tracer(False)
    turtle.penup()
    turtle.goto(0, Y_MIN)
    turtle.shape('arrow')
    turtle.setheading(270)
    turtle.stamp()
    turtle.write('    ' + str(Y_MIN))
    turtle.pendown()
    turtle.goto(0, Y_MAX)
    turtle.setheading(90)
    turtle.stamp()
    turtle.write('    ' + str(Y_MAX))
    steps = (Y_MAX - Y_MIN) // Y_GRID_LINE
    for y in range(Y_MIN, Y_MAX, steps):
        if y == Y_MIN:
            continue
        draw_y_tick(y)
    turtle.tracer(True)


def graph(f, color):
    '''This function sets the scaling of the window and draws the X and Y axes

    Parameters
    ----------
    f : function
        A mathematical function that will be plotted as y = f(x)
    color : string
        The name of a color that will be used to draw the line
    '''
    turtle.penup()
    turtle.hideturtle()
    turtle.speed(0)
    turtle.pencolor(color)  # We changed this line to use the argument color
                            # instead of always using the fixed value 'blue'
    turtle.pensize(3)
    for x in range(X_MIN, X_MAX):
        y = f(x)  # We changed this line to plot the argument f instead of
                  # the fixed function x ** 2
        turtle.goto(x, y)
        turtle.pendown()


def set_window():
    '''This function plots a mathematical function on the graph'''
    x_size = X_MAX - X_MIN
    x_margin = 0.1 * x_size

    y_size = Y_MAX - Y_MIN
    y_margin = 0.1 * y_size

    turtle.setworldcoordinates(X_MIN - x_margin,
                               Y_MIN - y_margin,
                               X_MAX + x_margin,
                               Y_MAX + y_margin)
    draw_x_axis()
    draw_y_axis()


set_window()
# Now we can plot as many functions as we want in different color
graph(func1, 'blue')
graph(func2, 'red')
