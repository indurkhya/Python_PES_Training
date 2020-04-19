# Strings Write a program to search an element in the list. i.e.
# Perform the binary search on the sorted list having integers as elements. If the search is successful print "Success"
# else print "un successful search".
#
lis = [35,25,75,45,65,55]
sort = sorted(lis)
print(sort)
for item in sort:
    if item in sort:
        print("Success")
    else:
        print("Un successful search")


