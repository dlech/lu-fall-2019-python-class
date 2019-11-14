# File: demo2.py
# Author: David Lechner
# Date: 11/5/2019

'''Demonstrate how coordinate system works in turtle graphics.

This is just for demonstrating how the coordinate system works in turtle
graphics. We don't need to understand how all of the parts of the program
work yet.

Run the program. Click anywhere in the window to advance to the next step It
shows how the coordinate system is layed out. It should be familiar because it
is what we learned in math class. The X axis is horizontal. The Y axis is
vertical. Measuring angles starts on the positive X axis and rotates
counterclockwise.

By default, each number on the axis represents one pixel on the screen.
'''

import asyncio
import math
import turtle

FONT = ('Ariel', 16, 'bold')

turtle.title('Turtle Coordinate System')


# asyncio event loop integration

click_event = asyncio.Event()
turtle.onscreenclick(lambda x, y: click_event.set())


def wait_for_click():
    click_event.clear()
    return click_event.wait()


async def update():
    while True:
        try:
            turtle.update()
        except turtle.Terminator:
            break
        await asyncio.sleep(0.1)



# drawing functions

def draw_x_axis():
    turtle.penup()
    turtle.goto(-200, 0)
    turtle.pendown()
    turtle.setheading(180)
    turtle.stamp()
    turtle.goto(200, 0)
    turtle.setheading(0)
    turtle.stamp()
    turtle.write('X', font=FONT)

def draw_y_axis():
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()
    turtle.setheading(270)
    turtle.stamp()
    turtle.goto(0, 200)
    turtle.setheading(90)
    turtle.stamp()
    turtle.write('Y', font=FONT)

def show_turtle(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.shape('turtle')
    turtle.showturtle()


# main program

async def run():
    turtle.hideturtle()

    turtle.pencolor('black')
    draw_x_axis()
    await wait_for_click()

    turtle.penup()
    turtle.pencolor('blue')
    turtle.goto(225, -12)
    turtle.write('+', font=FONT)
    turtle.goto(-225, -12)
    turtle.write('-', font=FONT)
    await wait_for_click()

    turtle.pencolor('black')
    draw_y_axis()
    await wait_for_click()

    turtle.penup()
    turtle.pencolor('blue')
    turtle.goto(-12, 225)
    turtle.write('+', font=FONT)
    turtle.goto(-12, -225)
    turtle.write('-', font=FONT)
    await wait_for_click()

    turtle.pencolor('green')

    for x, y in [(0, 0), (100, 100), (-100, 100), (-100, -100), (100, -100)]:
        show_turtle(x, y)
        turtle.write(f'   {(x, y)}', font=FONT)
        await wait_for_click()
        turtle.undo()

    for theta in range(0, 360 + 1):
        rad = 2 * math.pi * theta / 360
        x = 100 * math.cos(rad)
        y = 100 * math.sin(rad)

        turtle.tracer(False)
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(25, 0)
        turtle.pendown()
        turtle.circle(25, theta)
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.goto(x, y)
        turtle.tracer(True)

        if theta % 45 == 0:
            turtle.setheading(theta)
            show_turtle(x, y)
            turtle.write(f'   {theta}°', font=FONT)
            await wait_for_click()
            for _ in range(3):
                turtle.undo()
        else:
            await asyncio.sleep(turtle.delay() / 1000)

        turtle.tracer(False)

        for _ in range(8):
            turtle.undo()
        turtle.tracer(True)

    turtle.bye()


def main():
    loop = asyncio.get_event_loop()
    loop.create_task(run())
    loop.run_until_complete(update())


if __name__ == '__main__':
    main()
