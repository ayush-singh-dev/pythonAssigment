# 10. Write a program to repeat a tuple n times
user_input = tuple(map(int, input("Enter integers for the tuple: ").split()))
n = int(input("Enter the number of times to repeat the tuple: "))
repeated_tuple = user_input * n
print("Repeated tuple:", repeated_tuple)
