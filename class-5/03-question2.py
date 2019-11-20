# File: question2.py
# Author: David Lechner
# Date: 11/19/2019

'''Ask some questions about tomorrow'''

early = input('Do you have to get up early tomorrow? (y/n)')
alarm = input('Is your alarm clock set? (y/n)')

# LEARN: We can use the keyword `and` to make logical statements that depend
# on two conditions being true instead of one.

# we read this as "if we *do* have to get up early tomorrow and the alarm *is not* set then..."
if early == 'y' and alarm == 'n':
    # This indented code block will only run if both `==` expressions are true
    print('You better not forget to set your alarm!')

# we read this as "if we *do* have to get up early tomorrow and the alarm *is* set then..."
if early == 'y' and alarm == 'y':
    print('You are ready for tomorrow')

# we read this as "if we *do not* have to get up early tomorrow and the alarm *is* set then..."
if early == 'n' and alarm == 'y':
    print('You should turn off your alarm so you can sleep in')

# we read this as "if we *do not* have to get up early tomorrow and the alarm *is not* set then..."
if early == 'n' and alarm == 'n':
    print('Enjoy sleeping late')
