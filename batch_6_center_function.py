user_input = input("Enter text: ")
width_input = input("Enter digit of desired width: ")
fill_char = input("Enter [*] to pad with the string: ")

width = int(width_input)
centered_text = user_input

if len(fill_char) != 1:
    print("Padding character must be one character long")
    exit()

text_len = len(user_input)
total_padding = width - text_len

if total_padding <= 0:
    centered_text = user_input
else:
    left_padding_count = total_padding // 2
    right_padding_count = total_padding - left_padding_count

    left_side_padding = fill_char * left_padding_count
    right_side_padding = fill_char * right_padding_count
    centered_text = left_side_padding + user_input + right_side_padding

print(centered_text)