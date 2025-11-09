# 28. Write a program to find and display the highest marks from a CSV file.
import csv
with open("output.csv", "r") as f:
    reader = csv.DictReader(f)
    highest_age = -1
    for row in reader:
        age = int(row['Age'])
        if age > highest_age:
            highest_age = age
print(f"The highest age in the CSV file is: {highest_age}")
