# 16. Write a program to check if a set is a superset of another set.

set_A = {1, 2, 3, 4, 5}
set_B = {2, 3, 4}

if set_A.issuperset(set_B):
    print("Set A is a superset of Set B.")
else:
    print("Set A is NOT a superset of Set B.")
