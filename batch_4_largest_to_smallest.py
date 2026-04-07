entered_numbers = []

while True:
    try:
        entered_numbers.append(float(input("Enter a number: ")))
        entered_numbers.sort(reverse=True)
        print("The current order of the numbers are: ", entered_numbers)
    except ValueError:
        print("Invalid input. Stopping loop")
        break