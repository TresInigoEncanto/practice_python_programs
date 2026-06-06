user_input = input("Enter string: ")
width_input = input("Enter desired width: ")
fill_char = input("Enter [0] to pad with the string: ")

target_width = int(width_input)

current_len = len(user_input)

padded_text = user_input

if target_width > current_len:
    padding_needed = target_width - current_len

    for i in range(padding_needed):
        padded_text = padded_text + fill_char

print(f"Result: [{padded_text}]")