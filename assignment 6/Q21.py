# 21. Write a program to count distinct elements from a list using a set.
set_list = [1, 2, 2, 3, 4, 4, 5, 1, 6]
distinct_elements = set(set_list)
distinct_count = len(distinct_elements)
print("Number of distinct elements:", distinct_count)