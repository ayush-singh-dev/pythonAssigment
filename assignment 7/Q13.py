# 13. Write a program to read numbers from a file and display their sum and average.
f = open("numbers.txt", "r")
numbers = [int(line.strip()) for line in f]
f.close()
total = sum(numbers)
average = total / len(numbers) if numbers else 0
print(f"Sum: {total}, Average: {average}")