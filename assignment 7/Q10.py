# 10. Write a program to read a file and convert its content to uppercase.
f = open("sample.txt", "r")
content = f.read()
f.close()
content_upper = content.upper()
f = open("sample.txt", "w")
f.write(content_upper)
f.close()
print("File content converted to uppercase successfully.")
