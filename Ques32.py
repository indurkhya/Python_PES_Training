# Write a program to perform following operations on List. Create three lists as List1, List2 and List3 having 5
# city names each list.
# a. Find the length city of each list element and print city and length
# b. Find the maximum and minimum string length element of each list
# c. Compare each list and determine which city is biggest & smallest with length.
# d. Delete first and last element of each list and print list contents.

# a. Find the length city of each list element and print city and length
lis1 = ["Bhopal","Jabalpur","India","Katni","Bangalore"]
lis2 = ["Bhopal","Jabalpur","India","Katni","Bangalore"]
lis3 = ["Bhopal","Jabalpur","India","Katni","Bangalore"]

for item in lis1:
    print("City is: ",item,"length is: ",len(item))
for item in lis2:
    print("City is: ",item,"length is: ",len(item))
for item in lis3:
    print("City is: ",item,"length is: ",len(item))


# b. Find the maximum and minimum string length element of each list
# c. Compare each list and determine which city is biggest & smallest with length.

a = ["Bhopal","Jabalpur","India","Katni","Bangalore"]
b = ["Bhopal","Jabalpur","India","Katni","Bangalore"]
c = ["Bhopal","Jabalpur","India","Katni","Bangalore"]

print("**********************************************************************************************************")
lis = []
for item in a:
    length = len(item)
    lis.append(length)
print("The maximum string length element ",max(lis))
print("The minimum string length element ",min(lis))
minpos = lis.index(min(lis))
maxpos = lis.index(max(lis))
print("The maximum is at position", maxpos)
print("The minimum is at position", minpos)
print("**********************************************************************************************************")
for item in b:
    length = len(item)
    lis.append(length)

print("The maximum string length element ",max(lis))
print("The minimum string length element ",min(lis))
minpos = lis.index(min(lis))
maxpos = lis.index(max(lis))
print("The maximum is at position", maxpos)
print("The minimum is at position", minpos)

print("**********************************************************************************************************")
#
for item in c:
    length = len(item)
    lis.append(length)

print("The maximum string length element ",max(lis))
print("The minimum string length element ",min(lis))
minpos = lis.index(min(lis))
maxpos = lis.index(max(lis))
print("The maximum is at position", maxpos)
print("The minimum is at position", minpos)

print("**********************************************************************************************************")
# d. Delete first and last element of each list and print list contents.

ab = ["Bhopal","Jabalpur","India","Katni","Bangalore"]
#
print(ab)
for i in range(0,len(ab)):

    if ab[i]==ab[0]:
        ab.remove(ab[0])
        print(ab)
    else:
        break

for i in range(0,len(ab)):

    if ab[i]==ab[len(ab)-1]:
        ab.pop()
        print(ab)


