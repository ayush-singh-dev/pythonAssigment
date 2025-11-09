# 20. Write a program to merge two text files into a third file.

f1 = open("file1.txt", "r")
f2 = open("file2.txt", "r")
f3 = open("merged.txt", "w")
f3.write(f1.read())
f3.write(f2.read())
f1.close()
f2.close()
f3.close()
print("Files merged successfully.")
