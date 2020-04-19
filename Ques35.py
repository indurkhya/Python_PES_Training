# Create Tuple as specified below;
# a) Create a Tuple tup1 with days in a week & print the tuple elements
# b) Create a Tuple tup2  with months in a year and concatenate it with tup1
# c) Create 3 tuples( tup1,tup2,tup3) with numbers and determine which is greater.
# d) Try to delete an individual element in tup1 and try deleting complete Tuple -tup1 notice the error type you get.
# e) Insert new element in to tuple by typecasting it to List

tup1 = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
print(tup1)

tup2 = ("January","February","March","April","May","June","July","August","September","October","November","December")
print(tup2+tup1)

t1 = (42,15,35,25)
print(max(t1))
t2 = (15,85,75,45)
print(max(t2))
t3 = (95,68,98,68)
print(max(t3))
# for i in tup1:
#     del tup1[i]
#     print(i)
# print(tup1)
tup1 = list(tup1)
tup1.insert(7,"Welcome")
print(tup1)






