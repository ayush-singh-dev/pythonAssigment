# 3. Write a program to find the length of a tuple.
user_input = input("enter numbers: ")
tup = list(map(int,user_input.split()));
find_length = len(tup)
print("length of tuple is: ",find_length) 