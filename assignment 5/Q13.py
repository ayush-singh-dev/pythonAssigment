# 13. Write a program to find the maximum and minimum values in a tuple.
numbers = (5, 4, 3, 6, 2, 1, 9, 9)

min_value = numbers[0]
max_value = numbers[0]

for i in numbers:
    if i < min_value:
        min_value = i
    if i > max_value:
        max_value = i


print("Minimum value:", min_value)
print("Maximum value:", max_value)
