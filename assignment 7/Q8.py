# 8. Write a program to append new content to an existing file.
f = open("sample.txt", "a")
new_content = "\nThis is the appended line."
f.write(new_content)
f.close()
print("New content appended successfully.")
