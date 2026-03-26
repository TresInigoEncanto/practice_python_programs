entered_numbers = set()

while True:
    try:
        number_entered = float(input("Enter a number: "))

        if number_entered in entered_numbers:
            print(number_entered, "is Duplicate")
        else:
             print(number_entered, "is Unique")
             entered_numbers.add(number_entered)

    except ValueError:
        print("Invalid input, stopping loop")
        break
