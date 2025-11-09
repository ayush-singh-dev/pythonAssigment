# 7. Write a program to write multiple lines of input from the user into a file.
f = open("user_input.txt", "w")
print("Enter multiple lines of text (type 'STOP' to end):")
while True:
    line = input()
    if line == "STOP":
        break
    f.write(line + "\n")
f.close()
print("User input written to file successfully.")
