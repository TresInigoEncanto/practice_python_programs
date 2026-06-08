user_input = input("Enter text: ")
width_input = input("Enter desired width: ")

desired_width = int(width_input)
current_len = len(user_input)

sign = ""
clean_text = user_input

if current_len > 0:
    if user_input[0] == "-" or user_input == "+":
        sign = user_input[0]
        clean_text = user_input[1:]

if desired_width > current_len:
    padding_needed = desired_width - current_len

    zeros = ""
    for i in range(padding_needed):
        zeros += "0"
