# 15. Write a program to replace a word in a file with another word.

word_to_replace = "example"
replacement_word = "sample"
f = open("sample.txt", "r")
content = f.read()
f.close()
content = content.replace(word_to_replace, replacement_word)
f = open("sample.txt", "w")
f.write(content)
f.close()
print(f"'{word_to_replace}' replaced with '{replacement_word}' successfully.")
