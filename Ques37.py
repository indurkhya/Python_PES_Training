# Create 3 dictionaries (dict1, dict2, dict3) with 3 elements each. Perform following operations
# a) Compare dictionaries to determine the biggest.
# b) Add new elements in to the dictionaries dict1, dict2
# c) print the length of dict1, dict2, dict3.
# d) Convert dict1, dict2, and dict3 dictionaries as string and concatenate all strings together.

dict1 = {"Name":"Saksham","Roll_No":94,"Marks":90}
dict2 = {"Name":"Shashank","Roll_No":58,"Marks":91}
dict3 = {"Name":"Rohan","Roll_No":65,"Marks":75}

# a) Compare dictionaries to determine the biggest.
# dicA = str(dict1)
if dict1==dict2:
    print("The dict1 and dict2 are equal ")
elif dict1==dict3:
    print("The dict1 and dict3 are equal ")
elif dict2==dict3:
    print("The dict2 and dict3 are equal ")
else:
    print("Nothing are equal")

# print(dir(dict))
print(str(dict1))

# b) Add new elements in to the dictionaries dict1, dict2
dict1["Location"]="Jabalpur"
# print(dict1)
dict2["College"]="Bits Plani"
# print(dict2)
# c) print the length of dict1, dict2, dict3.
# print(len(dict1))
# print(len(dict2))
# print(len(dict3))

# d) Convert dict1, dict2, and dict3 dictionaries as string and concatenate all strings together.

str1 = str(dict1)
str2 = str(dict2)
str3 = str(dict3)

final_str = str1+str2+str3
print(final_str)
print(type(final_str))