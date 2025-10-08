# 20. Write a program to find the length of the longest word in a tuple.


tup = ("apple", "banana", "cherry", "mango", "grapefruit")

longest_word = ""
max_length = 0

for word in tup:
    if len(word) > max_length:
        max_length = len(word)
        longest_word = word

print("Tuple:", tup)
print("Longest word:", longest_word)
print("Length of longest word:", max_length)
