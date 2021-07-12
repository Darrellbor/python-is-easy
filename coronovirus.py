"""
    Title: importing.py
    Description: This file demonstrates my understanding of the 
    importing section of python is easy course
"""

from turtle import * 

color('green')
bgcolor('black')
speed(6)
hideturtle()
b = 0
while b < 200:
    left(b)
    forward(b * 2.5)
    b += 1
