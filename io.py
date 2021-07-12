"""
    Title: io.py
    Description: This file demonstrates my understanding of the 
    input and output (i/o) section of python is easy course
"""
import os

def noteTaking():
    filename = input('Enter a filename: ')

    if os.path.isfile(filename):
        print('What action would you like to perform? \n')
        prompt = input(' a) Read the file \n b) Delete the file and start over \n c) Append the file \n')

        if prompt == 'a':
            file = open(filename, 'r')
            for line in file:
                print(line, '\n')
            file.close()
        elif prompt == 'b':
            os.remove(filename)
            file = open(filename, 'w')
            file.write('')
            file.close()
        else:
            content = input('Enter the text you want to append to file {}: '.format(filename))
            file = open(filename, 'a')
            file.write('\n'+content)
            file.close()
    else:
        text = input('Enter the text that you want to write to the file: ')
        file = open(filename, 'w')
        file.write(text)
        file.close()

noteTaking()