# file: turtle2.py
# author: David Lechner
# date: 11/07/2019

'''Learning how to use the value in a for loop'''

import turtle

def triangle(side):
    for _ in range(3):
        turtle.forward(side)
        turtle.left(120)

turtle.speed(0)
turtle.pensize(3)

# LEARN: So far, we have been using "_" as a placeholder in our for loops. But
# really, it is variable that hold the value of each number in the sequence.

# LEARN: We can give this value any name we like. Here, we call it "n".

# LEARN: We need to learn how to count like a computer. If people count to 3, we
# say, "1, 2, 3". But computers always start counting with 0 instead of 1. So
# when a computer counts to 3, it says "0, 1, 2".

for n in range(12):
    triangle(50 + 8 * n)
    turtle.left(360 / 12)

# The first time the loop runs, the value of n is 0. So the side of the triangle
# will be 50 + 8 * 0 = 50 pixels.

# The second time the loop runs, the value of n is 1, so the side of the triangle
# will be 50 + 8 * 1 = 58 pixels.

# This continues until the last (12th) number. The value of n is 11 (not 12
# because we started counting with 0!). So the side of the triangle will be
# 50 + 8 * 11 = 138 pixels.

# Since we rotate the triangle and it gets bigger each time we go through the
# loop, this makes a shell patten.
