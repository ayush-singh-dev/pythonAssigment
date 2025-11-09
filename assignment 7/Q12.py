# 12. Write a program to count the occurrence of a specific word in a file.
word_to_count = "example"
f = open("sample.txt", "r")
content = f.read()
f.close()
word_count = content.count(word_to_count)
print(f"'{word_to_count}' found {word_count} times in the file.")