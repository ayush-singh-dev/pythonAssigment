# 2. Write a program to read the entire content of a text file.
f = open("sample.txt", "r")
print(f.read())
f.close()
print("File read successfully.")