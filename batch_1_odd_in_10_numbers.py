odd_numbers = 0

for i in range(1, 11):
    number = float(input("Enter a number: "))
    if number % 2 != 0:
        odd_numbers += 1
print(f"The number of odd numbers are {odd_numbers:.2f}")