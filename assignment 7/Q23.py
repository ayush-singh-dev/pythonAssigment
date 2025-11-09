# 23. Write a program to read a CSV file and calculate the average of numeric columns.
import csv
with open("output.csv", "r") as f:
    reader = csv.reader(f)
    headers = next(reader)
    sums = [0] * len(headers)
    counts = [0] * len(headers)

    for row in reader:
        for i in range(len(row)):
            try:
                value = float(row[i])
                sums[i] += value
                counts[i] += 1
            except ValueError:
                continue
    averages = [sums[i] / counts[i] if counts[i] > 0 else 0 for i in range(len(headers))]
    for i in range(len(headers)):
        print(f"Average of column '{headers[i]}': {averages[i]}")

