# File: 01-calc.py
# Author: David Lechner
# Date: 11/12/2019

'''Learning how to use python as a calculator'''

# basic math functions are built-in, but more functions available in the
import math

# LEARN: print() is a built-in function that writes text to the output terminal

# LEARN: when we print a string, the output we see is exactly what is between
# the quotes

# LEARN: when we print a mathematical expression, the output we see is the
# "answer" after evaluating the expression

# Basic math operations: addition (+), subtraction (-), multiplication (*),
# division (/)

print('1 plus 3 is', 1 + 3)  # OUTPUT: 1 plus 3 is 4
print('6 minus 3 is', 6 - 3)  # OUTPUT: 6 minus 3 is 3
print('2 times 3 is', 2 * 3)  # OUTPUT: 2 times 3 is 6
print('9 divided by 4 is', 9 / 4)  # OUTPUT: 9 divided by 4 is 2.25

# There are also special operator for integer division. // does division like /
# but it cuts off everything after the decimal point. % is called the "modulo"
# operator (or the shorter version "mod"). It returns the remainder after
# dividing.

print('9 divided by 4 is', 9 // 4, 'remainder', 9 % 4)
# OUTPUT: 9 divided by 4 is 2 remainder 1

# ** means "raised to the power of"

print('3 to the power of 2 is', 3 ** 2)  # OUTPUT: 3 to the power of 2 is 9

# Python also uses the same order of operations that we learned in math class

# multiplication/division before addition/subtraction
print(2 + 3 * 4)  # OUTPUT: 14
# parentheses first
print((2 + 3) * 4)  # OUTPUT: 20
# exponents before multiplication/division
print(2 * 3 ** 4)  # OUTPUT: 162

# Many more math functions are available in the math module as well as some
# useful constants, like π.

print('the square root of 9 is', math.sqrt(9))  # OUTPUT: the square root of 9 is 3.0
print('the log base 10 of 100 is', math.log10(100))  # OUTPUT: the log base 10 of 100 is 2.0
print('the cosine of pi is', math.cos(math.pi))  # OUTPUT: the cosine of pi is -1.0


# making a simple calculator

# LEARN: t\There is also an input() function that is similar to print() except
# that is also waits for input from the terminal. The program will wait until
# you type something and press enter before continuing.

# LEARN: Variables are like variables in algebra. They are just a name that
# represents a value. In this case, the store the number that we type in.

# LEARN: When we tried to add the two numbers we typed in with n1 + n2, a
# strange thing happened. For example, if we typed in 4 for the first number
# and 5 for the second number, then n1 + n2 results in 45 (instead of 9 as
# expected). This is because the input() function gives us a string and not
# a nubmer. It turns out that Python can add strings too. In order to add n1
# as n2 as numbers, we have to tell Python to treat them as numbers. We do
# this by using the built-in float() function to convert what we type in to
# a decimal number.

n1 = input('what is the first number?')
n2 = input('what is the second number?')
print(n1, 'plus', n2, 'is', float(n1) + float(n2))

# OUTPUT:
# what is the first number?4
# what is the second number?5
# 4 plus 5 is 9.0
