# entered_numbers = {}

# while True:
#     try:
#         number_entered = float(input("Enter a number: "))

#         if number_entered in entered_numbers:
#             print(number_entered, "is Duplicate")
#         else:
#             entered_numbers.add(number_entered)

#     except ValueError:
#         print("Invalid input, stopping loop")
#         break

from collections import Counter

numbers = []
while True:
    try:
        numbers.append(float(input("Enter a Number: ")))
    except:
        print("Invalid input. Stopping loop.")
        break

if numbers:
    counts = Counter(numbers)
    most_duplicates = counts.most_common(1)[0][0]
    print("Most duplicates:", most_duplicates)