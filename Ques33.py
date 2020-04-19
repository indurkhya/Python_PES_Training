# Create a list with 7 elements and perform following operations. Let the list be initialized with List1 any 5 city
# names;
# a) Append a new city name to the List
# b) Insert a city name at 4th index position
# c) Sort the list and print all elements
# d) Sort the elements of the list in descending order.
# e) delete last three elements using pop operation

lis = ["Hello","Welcome","to","Python"]

# a) Append a new city name to the List
lis.append("India")
print(lis)
# b) Insert a city name at 4th index position
lis.insert(4,"Learn")
print(lis)
# c) Sort the list and print all elements
lis.sort()
print(lis)
# d) Sort the elements of the list in descending order.
lis.sort(reverse=True)
print(lis)
# e) delete last three elements using pop operation
for i in range(len(lis)-3):
    lis.pop()
    print(lis)
    