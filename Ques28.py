# Write a program to check how many vovals present in the given string.
# That is, count the number of " a e i o u" in the given string and print the numbers against each oval.
# Example:- "This is Python" Number of total ovals = 3, i = 2, o =1


txt = "Working in python feels awesome"
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
for item in txt:
    if "a" in item:
        count1 += 1
    elif "e" in item:
        count2 += 1
    elif "i" in item:
        count3 += 1
    elif "o" in item:
        count4 += 1
    elif "u" in item:
        count5 += 1

count = count1 + count2 + count3 + count4 + count5
print("a = ", count1)
print("e = ", count2)
print("i = ", count3)
print("o = ", count4)
print("u = ", count5)

print("The total number of vowels in given text is: ", count)


