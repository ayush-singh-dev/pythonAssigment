# 24. Write a program to count the number of rows and columns in a CSV file.
import csv
with open("output.csv", "r") as f:
    reader = csv.reader(f)
    rows = list(reader)
    row_count = len(rows)
    col_count = len(rows[0]) if rows else 0
print(f"Number of rows in the CSV file: {row_count}")
print(f"Number of columns in the CSV file: {col_count}")
