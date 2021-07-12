"""
    Title: Loops1.py
    Description: This file demonstrates my understanding of the 
    loops section 1 of python is easy course
"""

def isPrime(num):
    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2,num):
            if (num % i) == 0:
                #print(num,"is not a prime number")
                #print(i,"times",num//i,"is",num)
                return False
        else:
            #print(num,"is a prime number")
            return True
        
    # if input number is less than
    # or equal to 1, it is not prime
    else:
        #print(num,"is not a prime number")
        return False

def fizzBuzz(num):
    for i in range(num):
        if isPrime(i):
            print(i, 'Prime')
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)


fizzBuzz(100)