unique_numbers = set()

for index in range (0,10):
    numbers = float(input(f"Enter value {index + 1}: "))
    unique_numbers.add(numbers)

print("Numbers entered:", list(unique_numbers))