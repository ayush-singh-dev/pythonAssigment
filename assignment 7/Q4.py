# 4. Write a program to count the number of words in a text file.
f = open("sample.txt", "r")
content = f.read()
words = content.split()
word_count = len(words)
f.close()
print(f"Number of words in the file: {word_count}")
