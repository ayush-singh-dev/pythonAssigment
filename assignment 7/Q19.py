# 19. Write a program to sort all words in a file alphabetically and save to a new file.

f = open("sample.txt", "r")
words = f.read().split()
f.close()
words.sort()
f = open("sorted_words.txt", "w")
f.write("\n".join(words))
f.close()
print("Words sorted and saved successfully.")
