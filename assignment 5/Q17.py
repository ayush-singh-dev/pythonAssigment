# 17. Write a program to reverse a tuple.

tup = (1, 2, 3, 4, 5)


# Reverse manually
reversed_list = []
for i in range(len(tup)-1, -1, -1):
    reversed_list.append(tup[i])

# Convert back to tuple
reversed_tup = tuple(reversed_list)

print("Original tuple:", tup)
print("Reversed tuple:", reversed_tup)
