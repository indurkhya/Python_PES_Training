# Using the built-in functions on Numbers perform following operations
# a) Round of the given floating point number. Example:  n=0.543 then round it next decimal number, i.e n=1.0
# Use round() function
# b) Find out the square root of a given number. (Use sqrt(x) function)
# c) Generate random number between 0, and 1 ( use  random() function)
# d) Generate random number between 10 and  500. (Use uniform() function)
# e) Explore all Math and Random module functions  on a given number/ List

import math
# from math import sqrt
# from random import randint,uniform
import random
# a) Round of the given floating point number.
n = 16
# print(float(round(n)))

# a = 10
# b = 500
# def sqrt(n):
#     return pow(n)
print(sqrt(n))
print(randint(0,1))
print(uniform(10,500))


# f = open("data.txt", "w+")
# txt = "This is 1st line\n"
# f.writelines( txt )
# seq = " This is 2nd line\nThis is 3rd line"
# f.seek(0, 2)
# f.writelines( seq )

# myList = []
# for line in f:
#     myList.append(line)

# print(myList)
# f.close()

# try:
#   f = open("testfile", "r")
#   f.write("This is the test file for exception handling!!")
# except IOError:
#   print ("Error: could not find a file or read data")
# else:
#   print ("content is written in the file successfully")

num = 1

def func():
    num = 5
    num += 5
    # num1 = num1 + 1
    print(num)

func()
print(num)

# from random import choices
# randrange
print(random.randrange(50))
print(random.randrange(0,50,2))
# randint
print(random.randint(1,15))
# choice
seq = [14,25,35,12,54,28,65,28,95,34]
print(random.choice(seq))
print(choices(['red', 'black', 'green'], [18, 18, 2], k=6))
# uniform
print(random.uniform(10,50))
print(dir(random))
# shuffle
mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)
print(random.sample(mylist, k=2))
# print(dir(math))

x = 5.6

print(math.ceil(x))  # greater number than x will return
x = 5
print(math.factorial(x))
x = 5.6
print(math.floor(x)) # lesser number than x will return
# print(math.gcd(a,b))
print(math.isfinite(x))
x = 9.96
print(math.trunc(x))
