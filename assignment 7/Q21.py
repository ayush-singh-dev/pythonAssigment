# 21. Write a Python program to create and write data into a CSV file.
import csv
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]
with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)
print("Data written to CSV file successfully.")
