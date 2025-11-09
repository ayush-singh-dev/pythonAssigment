# 14. Write a program to display the longest line in a file.

f = open("sample.txt", "r")
lines = f.readlines()
f.close()
if lines:
    longest_line = max(lines, key=len)
    print("Longest line:")
    print(longest_line)
else:
    print("The file is empty.")
