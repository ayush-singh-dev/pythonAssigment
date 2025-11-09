# 22. Write a program to read data from a CSV file and display it.
import csv
with open("output.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        