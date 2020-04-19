# Create 3 Lists (list1, list2, list3) with integer and perform following operations
# a) Create Maxlist by taking 2 maximum elements from each list.
# b) Find average value from all the elements of Maxlist.
# c) Create a MinlIst by taking 2 minimum elements from each list
# d) Find the average value from all the elements of Minlist

lis1 = [12,5,24,15,35]
lis2 = [45,25,36,28,42]
lis3 = [75,84,25,15,96]
Maxlist=[]
#
# for i in range(len(lis1)):
lis1.sort()
Maxlist.append(lis1[-1])
Maxlist.append(lis1[-2])
# print(dir(list))
print("The two Maximum number is ",lis1[-1],lis1[-2])
lis2.sort()
Maxlist.append(lis2[-1])
Maxlist.append(lis2[-2])
print("The two Maximum number is ",lis2[-1],lis2[-2])
lis3.sort()
Maxlist.append(lis3[-1])
Maxlist.append(lis3[-2])
print("The two Maximum number is ",lis3[-1],lis3[-2])
print(Maxlist)

# b) Find average value from all the elements of Maxlist.
sum = 0
for i in Maxlist:
    sum += i
print(sum)
avg = sum/len(Maxlist)
print(avg)

# c) Create a MinlIst by taking 2 minimum elements from each list
Minlist=[]
#
# for i in range(len(lis1)):
lis1.sort()
Minlist.append(lis1[0])
Minlist.append(lis1[1])
# print(dir(list))
print("The two Maximum number is ",lis1[0],lis1[1])
lis2.sort()
Minlist.append(lis2[0])
Minlist.append(lis2[1])
print("The two Maximum number is ",lis2[0],lis2[1])
lis3.sort()
Minlist.append(lis3[0])
Minlist.append(lis3[1])
print("The two Maximum number is ",lis3[0],lis3[1])
print(Minlist)

# d) Find the average value from all the elements of Minlist
sum = 0
for i in Minlist:
    sum += i
print(sum)
avg = sum/len(Minlist)
print(avg)