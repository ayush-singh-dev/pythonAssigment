# 14. Write a program to calculate the sum of numeric elements in a tuple.
numbers = (5, 4, 3, 6, 2, 1, 9, 9)

sum_of_numbers = 0

for i in numbers:
    sum_of_numbers += i

print("Sum of numeric elements:", sum_of_numbers)
