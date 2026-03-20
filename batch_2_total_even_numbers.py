even_numbers = 0

for index in range (0,10):
    numbers = float(input(f"Enter value {index + 1}: "))
    if(numbers % 2 == 0):
        even_numbers += 1

print("The total of even numbers in the list is", even_numbers)
