# 1. Write a Python program to create and write text into a file.
f = open("sample.txt", "w")
f.write("Hello, this is a test file.\nWelcome to Python file handling.")
f.close()
print("File created and written successfully.")
