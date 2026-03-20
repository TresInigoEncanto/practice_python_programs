first_number = float(input("Enter Value 1: "))

running_total = 0

for index in range (1,10):
    remaining_numbers = float(input(f"Enter value {index + 1}: "))
    running_total += remaining_numbers

difference = float(first_number - running_total)

print(f"The difference of the first number and the nine numbers is {difference:.2f}")