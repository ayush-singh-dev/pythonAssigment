# 6. Write a program to display only even-numbered lines from a file.
f = open("sample.txt", "r")
lines = f.readlines()
for i in range(1, len(lines), 2):
    print(lines[i].strip())
f.close()
