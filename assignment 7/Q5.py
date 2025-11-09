# 5. Write a program to count the number of lines and characters in a file.
f = open("sample.txt", "r")
lines = f.readlines()
line_count = len(lines)
char_count = sum(len(line) for line in lines)
f.close()
print(f"Number of lines in the file: {line_count}")
print(f"Number of characters in the file: {char_count}")
