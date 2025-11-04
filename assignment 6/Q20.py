# 20. Write a program to find the Cartesian product of two sets.
set_A = {1, 2, 3}
set_B = {4, 5, 6}

for a in set_A:
    for b in set_B:
        print(f"({a}, {b})")

