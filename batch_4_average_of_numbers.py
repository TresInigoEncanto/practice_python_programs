entered_numbers = []

while True:
    try:
        entered_numbers.append(float(input("Enter a number: ")))
        print("Running Average:", sum(entered_numbers) / len(entered_numbers))

    except ValueError:
        print("Invalid input. Stopping Loop")
        break