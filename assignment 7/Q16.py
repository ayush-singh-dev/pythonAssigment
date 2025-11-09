# 16. Write a program to display the first and last lines of a file.
f = open("sample.txt", "r")
lines = f.readlines()
f.close()
if lines:
    print("First line:")
    print(lines[0])
    print("Last line:")
    print(lines[-1])
else:
    print("The file is empty.")
