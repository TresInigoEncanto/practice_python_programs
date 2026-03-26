entered_numbers = set()

while True:
    try:
        number_entered = float(input("Enter a number: "))
        entered_numbers.add(number_entered)

        print(f"The smallest number is {min(entered_numbers)}")
        
    except ValueError:
        print("Invalid input, stopping program")
        break