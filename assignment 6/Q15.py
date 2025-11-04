# 15. Write a program to check if a set is a subset of another set.

set_A = {1, 2, 3, 4, 5}
set_B = {2, 3, 4}

if set_B.issubset(set_A):
    print("Set B is a subset of Set A.")
else:
    print("Set B is NOT a subset of Set A.")
