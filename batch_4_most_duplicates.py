from collections import Counter

numbers = []
while True:
    try:
        numbers.append(float(input("Enter a Number: ")))

    except ValueError:
        print("Invalid input. Stopping loop.")
        break

if numbers:
    counts = Counter(numbers)
    most_duplicates = counts.most_common(1)[0][0]
    print("Most duplicates:", most_duplicates)