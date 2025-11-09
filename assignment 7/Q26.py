# 26. Write a program to copy data from one CSV file to another.
import csv
with open("output.csv", "r") as source_file:
    reader = csv.reader(source_file)
    with open("copy_output.csv", "w", newline="") as dest_file:
        writer = csv.writer(dest_file)
        for row in reader:
            writer.writerow(row)
print("Data copied from output.csv to copy_output.csv successfully.")
