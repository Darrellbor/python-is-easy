"""
    Title: If Conditional.py
    Description: This file demonstrates my understanding of the 
    if statements section of python is easy course
"""

#Function to handle checking equality
def equal(val1, val2, val3 = ''):
    if(val3 and val3 != ''):
        return int(val1) == int(val2) or int(val1) == int(val3) or int(val2) == int(val3)
    else:
        return int(val1) == int(val2)

#Function to handle checking if 2 or more values are equal
def greater(a, b, c):
    if equal(a, b) or equal(b, c) or equal(a, b, c):
        return True
    else:
        return False

#Block to print calls to greater
print('Is Equal (1, 5, 3): ', greater(1, 5, 3))
print('Is Equal (3, 6, 3): ', greater(3, 6, 3))
print('Is Equal (4, 4, 4): ', greater(4, 4, 4))