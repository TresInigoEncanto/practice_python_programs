user_input = input("Enter text: ")
width_input = input("Enter desired width: ")
fill_char = input("Enter [*] to pad with the string: ")

centered_text = user_input

if len(fill_char) != 1:
    print("Padding character must be one character long")


