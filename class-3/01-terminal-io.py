# File: 01-terminal-io.py
# Author: David Lechner
# Date: 11/12/2019

'''Learning how to use terminal for output and input'''

# LEARN: print() is a built-in function that writes text to the output terminal

# LEARN: when we print a string, the output we see is exactly what is between
# the quotes

print('Hello world')  # OUTPUT: Hello world

# LEARN: There is also an input() function that is similar to print() except
# that is also waits for input from the terminal. The program will wait until
# you type something and press enter before continuing with the rest of the
# program.

# LEARN: Variables are like variables in algebra. They are just a name that
# represents a value. In this case, the store whatever we type in.

name = input('What is your name?')
print('Hello', name)

# OUTPUT:
# What is your name?Student
# Hello Student
