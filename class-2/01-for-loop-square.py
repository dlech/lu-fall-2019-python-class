# file: 01-for-loop-square.py
# author: David Lechner
# date: 11/07/2019

'''How to use a for loop to draw a square'''

import turtle

# previously, we drew a square like this:

'''
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
'''

# The same 2 lines are repeated 4 times each.



# Instead of copying and pasting, we can tell Python to do the repeating for
# us by using the for keyword and the built-in range() function.

# LEARN: "for" is a keyword (and so is "in").

# LEARN: A for loop repeats the same block of code over a sequence of values

# LEARN: The range() function produces a sequence of values.

# LEARN: The indentation is important! After the ":", everything that is
# indented is called a "block" of code. The indentation has to be exactly the
# same for all lines! If one line has 3 spaces and one line has 4 spaces, it
# will cause an error.

# LEARN: Pressing the TAB key on the keyboard is a shortcut for entering 4 spaces.

for _ in range(4):
    turtle.forward(100)
    turtle.left(90)

# In this program, the range function produces 4 values (because we used 4 as
# the argument) so the loop repeats the code 4 times.
