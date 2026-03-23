unique_numbers = []

for index in range (0,10):
    numbers = float(input(f"Enter value {index + 1}: "))
    unique_numbers.append(numbers)

print("Unique numbers:")

for numbers in unique_numbers:
    if unique_numbers.count(numbers) == 1:
        print(numbers)