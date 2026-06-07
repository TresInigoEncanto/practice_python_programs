user_input = input("Enter text: ")

if user_input == "":
    result = ""

else:
    first_char = user_input[0]
    remaining_char = user_input[1:]

    first_char_caps = first_char.upper()
    remaining_chars_small = remaining_char.lower()

    result = first_char_caps + remaining_chars_small

print(result)

