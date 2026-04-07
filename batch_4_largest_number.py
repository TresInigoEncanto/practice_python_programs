entered_numbers = []

while True:
    try:
        entered_numbers.append(float(input("Enter a number: ")))
        largest_number = max(entered_numbers)
        print("The current largest number is:", largest_number)

    except ValueError:
        print("Invalid input. Stopping loop")
        break