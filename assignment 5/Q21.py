# 21. Write a program to create a nested tuple and access its elements.

nested_tup = (1, 2, (3, 4), (5, 6, (7, 8)))

# Accessing elements
print("Original nested tuple:", nested_tup)
print("Element at index 0:", nested_tup[0])
print("Element at index 2:", nested_tup[2])
print("Element at index 2, 0:", nested_tup[2][0])
print("Element at index 3, 2, 1:", nested_tup[3][2][1])
print("Element at index 3, 1:", nested_tup[3][1])