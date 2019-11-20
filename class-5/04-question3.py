# File: question3.py
# Author: David Lechner
# Date: 11/19/2019

'''Ask some questions about goats'''

# REVIEW: We write `NUM_GOATS` in all caps because it is a constant. We set it
# once at the begining of the program and don't change after that.

NUM_GOATS = 10  # This is how many goats I have

# REVIEW: The input() function gives us a string, but we need a number, so we
# use int() to convert what the user types in to an integer.

# TRY IT: What happens if the user types in a letter instead of a nubmer? What
# about a number with a decimal point?

answer = int(input('How many goats do you see?'))


# LEARN: We can use inequality operators to compare numbers

if answer < NUM_GOATS:
    print('Some of your goats are missing!')

if answer == NUM_GOATS:
    print('All of the goats are there.')

if answer > NUM_GOATS:
    print('You have extra goats!')
