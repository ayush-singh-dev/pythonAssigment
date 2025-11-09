# 3. Write a program to read a file line by line.
f = open("sample.txt", "r")
for line in f:
    print(line.strip())
f.close()
