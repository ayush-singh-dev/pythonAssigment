# 22. Write a program to find duplicate elements in a list using a set.

set_list = [1, 2, 3, 2, 4, 5, 1, 6, 4]
duplicates = set()
seen = set()
for item in set_list:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)
print("Duplicate elements are:", duplicates)
