entered_numbers = []

while True:
    try:
        number_entered = float(input("Enter a number: "))
        entered_numbers.append(number_entered)
        entered_numbers.sort()
        print(entered_numbers)
    except ValueError:
        print("Invalid input, stopping the program")