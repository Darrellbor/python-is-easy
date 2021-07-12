"""
    Title: Loops2.py
    Description: This file demonstrates my understanding of the 
    loops section 2 of python is easy course
"""

def drawGameBoard(rows, columns):
    for row in range(int(rows)):
        if row % 2 == 0:
            setColumns = int(columns)
            if(int(columns) % 2 != 0):
                setColumns = columns + 1
            for column in range(1, setColumns):
                if column % 2 == 1:
                    if column < int(columns) - 1:
                        print(" ", end="")
                    else:
                        print(" ")
                else:
                    print("|", end="")

        else: 
            setRows = int(rows)
            if(int(rows) % 2 == 0):
                setRows = rows + 1
            print("-"*setRows)
    print('\n')


drawGameBoard(5, 6)
drawGameBoard(22, 23)
drawGameBoard(45, 46)