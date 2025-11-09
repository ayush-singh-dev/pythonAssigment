# 18. Write a program to read a file and store only unique words into another file.

f = open("sample.txt", "r")
words = f.read().split()
f.close()
unique_words = set(words)
f = open("unique_words.txt", "w")
f.write("\n".join(unique_words))
f.close()
print("Unique words stored successfully.")
