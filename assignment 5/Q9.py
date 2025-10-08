# 9. Write a program to concatenate two tuples.
tuple1 = tuple(map(int, input("Enter integers for first tuple: ").split()))
tuple2 = tuple(map(int, input("Enter integers for second tuple: ").split()))
concatenated_tuple = tuple1 + tuple2
print("Concatenated tuple:", concatenated_tuple)
