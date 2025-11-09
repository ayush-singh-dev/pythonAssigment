# 25. Write a program to append a new record to an existing CSV file.
import csv
new_record = ["David", 28, "Miami"]
with open("output.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(new_record)
print("New record appended to CSV file successfully.")
