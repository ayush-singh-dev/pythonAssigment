# 26. Write a program to convert a tuple of tuples into a dictionary.

tup = (("a", 1), ("b", 2), ("c", 3))

dict_result = {}  # empty dictionary

for item in tup:
    key = item[0]
    value = item[1]
    dict_result[key] = value

print("Tuple of tuples:", tup)
print("Converted dictionary:", dict_result)
