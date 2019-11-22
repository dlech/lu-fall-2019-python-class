# File: guess.py
# Author: David Lechner
# Date: 11/21/2019

'''A guessing game.

This is the classic game where someone thinks of a secret number and someone
else tries to guess it. In this case, the computer thinks of the number and we
(the user) have to guess what it is.
'''

# LEARN: Python has a standard module for dealing with random numbers

import random

LOWEST = 1
# we change change this number to make the game easier (e.g. set to 10) or more
# difficult (e.g. set to 1000)
HIGHEST = 100

# This is the secret number. It will be different each time the program runs
# because we are using a random number generator.
NUMBER = random.randint(1, HIGHEST)

correct = False  # This variable tells us if the we guessed the correct number
count = 0  # This variable keeps track of how many guesses have been made

# LEARN: The `while` keyword is used to create a loop in the program. It
# repeats the code block as long as the condition is true.

# LEARN: The `not` keyword is a logic function that changes false to true and
# true to false.

# Since our program starts with correct = False, `not correct` is true and the
# code block inside the loop will run. It will keep repeating until `not correct`
# is false - in other words, it will keep repeating until correct is true.

while not correct:

    # LEARN: `try/except` blocks are used to handle errors without crashing the
    # program. In this case, if the user types in something that is not an
    # integer, the int() function will raise a ValueError exception. We can
    # catch this exception and handle the error so that our program doesn't
    # crash if the user types in 'bob', for example.

    try:
        # REVIEW: We can use `+` to add strings together. But we can't add
        # strings and numbers, so we use `str()` to convert numbers to strings
        # before adding them to other strings.

        answer = int(input('Guess a number between ' + str(LOWEST) + ' and '
                           + str(HIGHEST) + ': '))

        # LEARN: If an error occurred above, then the following line is skipped.
        # Instead, the program flow jumps to the `except ValueError` line.

        count += 1
    except ValueError:
        # LEARN: This block of code will run only if there was a ValueError
        # after the `try:` and before `except ValueError:`

        print('That is not a number. Try again.')

        # REVIEW: the continue keyword makes the program flow jump to the
        # beginning of the loop (the `while not correct:` line in this program)
        # instead of continuing with everything else below.

        continue

    # REVIEW: We use `if` to run blocks of code if a condition is true or skip
    # blocks of code if a condition is false.

    # LEARN: In addition to `if` and `else`, we can have an `elif` statement
    # (short for "else if"). We can use these to chain test conditions. Only
    # the blocks of code after the first condition that is true will run. All
    # other blocks will be skipped, even if they are also true.

    if answer < LOWEST or answer > HIGHEST:
        # This will run if the answer is less than the lowest possible number or
        # greater than the highest possible number
        print('That number is out of range')
    elif answer == NUMBER:
        # this will run only when the answer is the secret number
        correct = True
        print('You guessed correct!')
        print('It took', count, 'guesses')
    elif answer < NUMBER:
        # This will only run if the answer is less than the secret number and
        # greater than or equal to the lowest number. We didn't have to write
        # the second part (`answer >= LOWEST`) because of the `elif`.
        print('Too low. Try again.')
    else:
        # This will only run if the answer is greather than the secret number
        # and less than or equal to the highest possible number. We don't have
        # to write `elif answer > NUMBER or answer <= HIGHEST:` because it is
        # the only possibility left after all of the other test cases above.
        print('Too high. Try again.')


