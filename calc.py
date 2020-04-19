# Create file called  "calc.py" which has following functions
# i) functions to add 2 numbers
# ii) function to find diff of 2 numbers
# iii) function to multiply 2 numbers
# iv) all maths operations ( sqrt, div, floor div, modulus, primenumber)
# v) Fibonacci series

import math

def Add(a,b):
    return a + b

def diff(a,b):
    return a - b

def mul(a,b):
    return a * b

def Sqrt(a,b):
    val1 = math.sqrt(a)
    val2 = math.sqrt(b)
    return val1,val2

def Div(a,b):
    return a / b

def FloorDiv(a,b):
    return a // b

def Modulus(a,b):
    return a % b

def Prime(a):

    if a > 1:
        for i in range(2,a):
            if (a % i ==0):
                print(a," is not a prime number ")
                break
        else:
            print(a," is a prime number ")
    else:
        print("wrong input")

def Fibonacii(n):

    if n == 1:
        return 1

    elif n == 2:
        return 1

    else:
        return Fibonacii(n-1) + Fibonacii(n-2)



