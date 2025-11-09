# 11. Write a program to search for a particular word in a file.
word_to_search = "example"
f = open("sample.txt", "r")
content = f.read()
f.close()
if word_to_search in content:
    print(f"'{word_to_search}' found in the file.")
else:
    print(f"'{word_to_search}' not found in the file.")
