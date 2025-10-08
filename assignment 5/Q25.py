# 25. Write a program to find the difference between two tuples.
tup1 = (1, 2, 3, 4, 5)
tup2 = (4, 5, 6, 7)

difference_tup = tuple(set(tup1) - set(tup2))

print("Tuple 1:", tup1)
print("Tuple 2:", tup2)
print("Difference (tup1 - tup2):", difference_tup)
