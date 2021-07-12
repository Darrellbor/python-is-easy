"""
    Title: importing.py
    Description: This file demonstrates my understanding of the 
    importing section of python is easy course
"""

import random as rand
import math


randVal = rand.randint(0, 100)

while(True):
    guess = int(input('Guess a number between 1 and 100: '))

    if guess == randVal:
        break
    elif guess < randVal:
        print('Guess was too low')
    else:
        print('Guess was too high')

print('You guessed correct with value:', randVal)