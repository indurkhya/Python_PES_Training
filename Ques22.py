# Read the value x and y from the user and apply all trigonometric functions on these numbers. Note: Refer the tutorial Trigonometric operation table.

import math
# number
x = 45

# math.cos()
print("math.cos(",x,"): ", math.cos(x));

# math.sin()
print("math.sin(",x,"): ", math.sin(x));

# math.tan()
print("math.tan(",x,"): ", math.tan(x));

x =0.75

# math.acos()
print("math.acos(",x,"): ", math.acos(x));

# math.asin()
print("math.asin(",x,"): ", math.asin(x));

# math.atan()
print("math.atan(",x,"): ", math.atan(x));

y = 2
# math.atan2(y,x) = atan(y/x)
# print("math.atan2(",y,",",x,"): ", math.atan2(y,x))
math.hypot(x,y)
print("math.hypot(",x,",",y,"): ", math.hypot(x,y))