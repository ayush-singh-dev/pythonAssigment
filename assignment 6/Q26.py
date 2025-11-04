# 26. Write a program to find unique words in a sentence using a set.
sentence = "This is a test sentence and this test is only a test"
words = sentence.lower().split()
unique_words = set(words)
print("Unique words in the sentence:", unique_words)    