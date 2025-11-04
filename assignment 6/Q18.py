# 18. Write a program to remove all elements of one set from another set.
set_X = {1, 2, 3, 4, 5}
set_Y = {4, 5, 6, 7, 8}
set_X.difference_update(set_Y)
print("Set X after removing elements of Set Y:", set_X)
