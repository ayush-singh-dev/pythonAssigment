# 27. Write a program to unzip a list of tuples into individual lists.

list_of_tuples = [(1, "a"), (2, "b"), (3, "c")]

list1 = []
list2 = []

for t in list_of_tuples:
    list1.append(t[0])
    list2.append(t[1])

print("Original list of tuples:", list_of_tuples)
print("First list:", list1)
print("Second list:", list2)
