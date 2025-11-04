# 27. Write a program to check if two strings are anagrams using sets.

# Program to check if two strings are anagrams using sets

# Input two strings
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Remove spaces and convert to lowercase
str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

# Check if both strings have the same unique characters
if set(str1) == set(str2):
    print("The strings are anagrams (based on unique letters).")
else:
    print("The strings are NOT anagrams.")
