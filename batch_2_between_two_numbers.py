first_number = int(input("Enter your first number: "))
second_number = int(input("Enter your second number: "))

start = min(first_number, second_number)
end = max(first_number, second_number)

for number in range(start + 1, end):
    print(number)
