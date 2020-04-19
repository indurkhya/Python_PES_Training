# Write a program to Sort given N numbers (Use only loop structures and Conditions to
# sort the elements. Use Bubble sort / Selection sort technique to sort the elements of List)
# Note: Don't use built in functions to sort.

lis = [95, 24, 75, 35, 12]  # N numbers

# Traverse through all List elements
for i in range(len(lis)):
    # Find the minimum element in remaining
    # unsorted List
    min_idx = i
    for j in range(i + 1, len(lis)):
        if lis[min_idx] > lis[j]:
            min_idx = j

            # Swap the found minimum element with
    # the first element
    lis[i], lis[min_idx] = lis[min_idx], lis[i]

# Driver code to test above
print("Sorted List")
for i in range(len(lis)):
    print(lis[i],end=" ")