while True:
    try:
        numbers = float(input("Enter a number: "))
    except ValueError:
        print("Invalid input entered")
        break
