# 9. Write a program to copy the contents of one file into another.
source_file = open("sample.txt", "r")
destination_file = open("copy_sample.txt", "w")
for line in source_file:
    destination_file.write(line)
source_file.close()
destination_file.close()
print("File copied successfully.")
