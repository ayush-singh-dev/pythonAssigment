# 12. Write a program to convert a tuple into a string.

user_input = ('H', 'e', 'l', 'l', 'o')
result = "";

for char in user_input:
    result += str(char) 


print("result:  ",result)
print("type: ",type(result))

