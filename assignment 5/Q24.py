# 24. Write a program to find common elements between two tuples.
tup1 = (1, 2, 3, 4, 5, 6)
tup2 = (4, 5, 6, 7, 8, 9)

common_tup = tuple(set(tup1) & set(tup2))

print("Tuple 1:", tup1)
print("Tuple 2:", tup2)
print("Common elements:", common_tup)
