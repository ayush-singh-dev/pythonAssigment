# 30. Write a program to combine multiple CSV files into one single file.
import csv
import glob
csv_files = glob.glob("csv_files/*.csv")  # Assuming all CSV files are in 'csv_files' directory
with open("combined_output.csv", "w", newline="") as outfile:
    writer = csv.writer(outfile)
    for i, file in enumerate(csv_files):
        with open(file, "r") as infile:
            reader = csv.reader(infile)
            if i == 0:
                # Write header only once
                writer.writerow(next(reader))
            else:
                next(reader)  # Skip header for subsequent files
            for row in reader:
                writer.writerow(row)
print("CSV files combined into combined_output.csv successfully.")