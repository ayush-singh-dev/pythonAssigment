#2.  Write a program to create a tuple with different data types.

user_input1 = int(input("inter integer: "));
user_input2 = input("enter string");
user_input3 = list(map(int, input("enter list (space-separated numbers): ").split()));
user_input4 = float(input("Enter float: "))
tup1 = (user_input1,user_input2,user_input3)
print(tup1)