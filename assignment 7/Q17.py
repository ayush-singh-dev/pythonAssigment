# 17. Write a program to remove blank lines from a file.
f = open("sample.txt", "r")
lines = f.readlines()
f.close()
with open("sample.txt", "w") as f:
    for line in lines:
        if line.strip():
            f.write(line)
print("Blank lines removed successfully.")
