number_entered = [float(input(f"Enter Value {index + 1}: ")) for index in range (0, 10)]

seen = set()
duplicates = set()

for number in number_entered:
    if number in seen:
        duplicates.add(number)
    else:
        seen.add(number)

print("Duplicate numbers:", * duplicates)