# 22. Write a program to flatten a nested tuple.


tup = (1, (2, 3), (4, (5, 6)), 7)

stack = [tup]  
flat = []          

while stack:
    current = stack.pop(0)   
    for item in current:
        if isinstance(item, tuple):
            stack.insert(0, item)  
        else:
            flat.append(item)

flattened_tup = tuple(flat)

print("Original tuple:", tup)
print("Flattened tuple:", flattened_tup)
