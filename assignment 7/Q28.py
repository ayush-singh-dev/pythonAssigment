# 27. Write a program to display specific columns (like Name and Marks) from a CSV file.
import csv
with open("output.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"Name: {row['Name']}, Age: {row['Age']}, City: {row['City']}")

        