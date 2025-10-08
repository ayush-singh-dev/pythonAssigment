# 28. Write a program to find repeated items in a tuple.

tup = (1, 2, 3, 2, 4, 5, 1, 6, 3, 7)

repeated = []

for i in tup:
    if tup.count(i) > 1 and i not in repeated:
        repeated.append(i)

print("Tuple:", tup)
print("Repeated items:", tuple(repeated))