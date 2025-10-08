# 8. Write a program to find the index of an element in a tuple.

user_input = tuple(map(int, input("Enter integers: ").split()))

element = int(input("Enter element to find: "))

for i in range(len(user_input)):
    if user_input[i] == element:
        print(f"Element {element} found at index {i}")
        break
else:
    print(f"Element {element} not found in the tuple.")
