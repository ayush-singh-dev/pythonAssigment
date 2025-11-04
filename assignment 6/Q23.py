# 23. Write a program to remove duplicates from a list using a set.
input_list = [1, 2, 2, 3, 4, 4, 5, 1, 6]
unique_elements = set(input_list)
output_list = list(unique_elements)
print("List after removing duplicates:", output_list)