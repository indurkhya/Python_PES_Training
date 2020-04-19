# a) Write a new program in file "maths.py" such that you import functions of file "calc.py" to your new program
# b) Use From <module> import <function> statement to import only few function  from calc module.

from calc import Fibonacii
from calc import Prime

print(Fibonacii(7))

Prime(23)
# 0 1 1 2 3 5 8 13 21