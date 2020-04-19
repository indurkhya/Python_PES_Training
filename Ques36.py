# Create two tuples tup1 & tup2 and apply all built in functions on tuples. ( Refer Tutorial for the Built in functions list)

# print(dir(tuple))

tup = (42,54,18,62,74,15)

# Return 1 if the value exist and if the value is not exist the n it will return the value 0
print(tup.count("Saksham"))
print(tup.count(62))
print(tup.count(15))

# Using index
print(tup.index(62))
print(tup.index("Saksham"))
print(tup.index(18))


# len(object) → integer
print(len(tup))

# max( tuple ) → value
print(max(tup))

# min(tuple)
print(min(tup))

tup1 = (74,)
print(any(tup1))



