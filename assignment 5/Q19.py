# 19. Write a program to remove duplicate elements from a tuple.

tup = (5, 2, 3, 2, 5, 1, 4, 3, 1)

unique_list = []
for item in tup:
    if item not in unique_list:   
        unique_list.append(item)

unique_tup = tuple(unique_list)

print("Original tuple:", tup)
print("Tuple without duplicates:", unique_tup)
