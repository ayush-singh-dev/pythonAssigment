# 30. Write a program to perform all basic set operations (union, intersection, difference,
# symmetric difference) in one program.

# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union
union = set1 | set2
print("Union:", union)

# Intersection
intersection = set1 & set2
print("Intersection:", intersection)

# Difference
difference = set1 - set2
print("Difference:", difference)

# Symmetric Difference
symmetric_difference = set1 ^ set2
print("Symmetric Difference:", symmetric_difference)