# File: graph_calc.py
# Author: David Lechner
# Date: 11/14/2019

'''A graphing calculator using turtle graphics'''

import turtle

# LEARN: We use all CAPS to indicate that variables are "constants". This is
# not a strict rule, but it is a very common way to write Python code. It just
# means that we assign the value once and never change it for the rest of the
# program.

# LEARN: We put all of the constants at the beginning of the file (after imports)
# so that they are easy to find and change in case we need to make adjustments.

X_MIN = -100
X_MAX = 100
X_GRID_LINE = 10
Y_MIN = -10000 // 9
Y_MAX = 10000
Y_GRID_LINE = 10

# On the Y axis, we have make Y_MIN 1/9th of Y_MAX. Since we have 10 grid lines
# (Y_GRID_LINE = 10), this means that one grid line will fall exactly on the
# X axis.


def draw_x_tick(x):
    '''This draws a tick mark on the X axis

    Parameters
    ----------
    x : integer
        The position on the X axis where the tick mark should be drawn
    '''
    turtle.penup()
    turtle.goto(x, 0)  # This is the point where the tick mark crosses the X axis
    turtle.setheading(90)  # This turns the turtle so that the tick mark will be vertical

    # We want the height of the tick mark to be 4% of the height Y axis.
    # (Y_MAX - Y_MIN) gives us the height of the Y axis. Multiplying this by
    # 0.02 gives us 2% of the height of the Y axis.
    d = (Y_MAX - Y_MIN) * 0.02
    turtle.pendown()
    turtle.forward(d)  # This draws half of the tick mark above the X axis
    turtle.backward(2 * d)  # this retraces backwards twice the distance, which
                            # draws the other half of the tick mark below the X axis

def draw_y_tick(y):
    '''This draws a tick mark on the Y axis

    Parameters
    ----------
    y : integer
        The position on the Y axis where the tick mark should be drawn
    '''

    # This function is almost the same as draw_x_tick(). We just swap X for Y
    # everywhere.

    turtle.penup()
    turtle.goto(0, y)
    turtle.setheading(0)
    d = (X_MAX - X_MIN) * 0.02
    turtle.pendown()
    turtle.forward(d)
    turtle.backward(2 * d)


def draw_x_axis():
    '''This draws the horizontal X axis'''
    turtle.tracer(False)  # This turns off animation to make everything draw faster
    turtle.penup()
    turtle.goto(X_MIN, 0)  # We use the constant X_MIN instead of a number so that
                           # we don't have to change the number everywhere in our
                           # program if we decide we want a different number
    turtle.shape('arrow')
    # draw an arrow poiting left
    turtle.setheading(180)
    turtle.stamp()
    # Label the negative side of the X axis
    turtle.write('  ' + str(X_MIN))  # Python doesn't let us add a string and a
                                     # number, but it can add two strings, so
                                     # we convert X_MIN to a string with str()
    turtle.pendown()
    turtle.goto(X_MAX, 0)
    # draw an arrow pointing right
    turtle.setheading(0)
    turtle.stamp()
    # label the positive side of the X axis
    turtle.write('   ' + str(X_MAX))

    # X_GRID_LINE tells us how many tick marks to draw. So we have to divide
    # the total length of the X axis into that many segments. (X_MAX - X_MIN)
    # gives the total length of the X axis. So, if the X axis is 200 numbers
    # long and we want 10 grid lines, then each grid lines will be drawn at
    # every 20 numbers.
    steps = (X_MAX - X_MIN) // X_GRID_LINE

    # LEARN: the range function returns the value X_MIN, but does not return
    # the value X_MAX.

    for x in range(X_MIN, X_MAX, steps):
        # The first tick mark will be drawn where the arrow is, so we want to skip drawing it
        if x == X_MIN:
            continue  # this means go back to the begining of the for loop
        draw_x_tick(x)
    turtle.tracer(True)  #this shows everything above on the screen



def draw_y_axis():
    '''This draws the horizontal Y axis'''
    # This function is almost exactly like draw_x_axis() except X and Y are swapped
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


def set_window():
    '''This function sets the scaling of the window and draws the X and Y axes'''
    # X_MAX - X_MIN gives us the total size of the X axis
    x_size = X_MAX - X_MIN
    # We want to add a 10% margin to make it look nicer, otherwise the arrows
    # will go all the way to the edge of the window
    x_margin = 0.1 * x_size

    y_size = Y_MAX - Y_MIN
    y_margin = 0.1 * y_size

    # This changes the scaling of the coordinate system so that it shows
    # both the X and Y axis plus the extra margin on each side
    turtle.setworldcoordinates(X_MIN - x_margin,
                               Y_MIN - y_margin,
                               X_MAX + x_margin,
                               Y_MAX + y_margin)
    draw_x_axis()
    draw_y_axis()


def graph():
    '''This function plots a mathematical function on the graph'''
    turtle.penup()
    turtle.hideturtle()
    turtle.speed(0)
    turtle.pencolor('blue')
    turtle.pensize(3)

    for x in range(X_MIN, X_MAX):
        y = x ** 2  # we are plotting the function y = x squared
        turtle.goto(x, y)
        turtle.pendown()



# don't forget to call the functions!
set_window()
graph()
