# Write a program to count the occurrences of an element in a tuple.

user_input = tuple(map(int,input("inter interger: ").split()));
element = 5;
count = 0;

for value in user_input:
    if(element ==value):
        count +=1
print("numner of occurence: ",count)        