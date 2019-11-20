# File: question1.py
# Author: David Lechner
# Date: 11/19/2019

'''Ask a question about the weather'''

# REVIEW: The built-in input() function waits for the user to type something
# and press enter. The variable `answer` will contain whatever was type in
# (as a string).

answer = input('Is it sunny today? (y/n)')

# LEARN: An `if` statement asks the question: is the following true? The ==
# operator tests if two values are equal. So the following statement should
# be read as "if the answer the user typed in is equal to the string 'y'"
# then...

if answer == 'y':
    # If the statement above is true, then this indented code block will run
    # but if it is not true, this indented code block will be skipped
    print('you should wear sunglasses')

# LEARN: After an ``if statement, we can write an `else` statement

else:
    # This indented code block will only run if the code block between 'if'
    # and 'else' did not run
    print('it must be cloudy')
