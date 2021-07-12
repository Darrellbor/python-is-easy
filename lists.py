"""
    Title: Lists.py
    Description: This file demonstrates my understanding of the 
    lists section of python is easy course
"""

# Array definition & initialization to store unique values
myUniqueList = []
# Array definition & initialization to store left over values
myLeftovers = []

# Function to check for duplicates in a list
def checkForDuplicates(params):
    return len(params) != len(set(params))

# Function to check and add unique values to list and non-unique values 
# to left over vars and return either true or false
def addToListFunc(*args):
    params = list(args)

    for i in params:
        # Edge case to check for duplicates from the parameters
        if checkForDuplicates(params):
            return False
        elif i in myUniqueList:
            myLeftovers.append(i)
            return False
        else:
            myUniqueList.extend(params)
            return True

# Function to call that calls addToListFunc and formats response
def addToList(*args):
    isAdded = addToListFunc(*args)
    print('Value Were Added: ', isAdded, '\n', 'Unique List: ', myUniqueList, '\n', 'Left Overs: ', myLeftovers)


# Function calls to test implementation
addToList(1, 2, 3)
addToList(3, 2, 5)
addToList(45, 45, 76)
addToList(23, 90, 87)