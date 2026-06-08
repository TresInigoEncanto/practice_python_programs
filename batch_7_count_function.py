user_input = input("Enter text: ")
string_count = input("Enter substring to count: ")

input_len = len(user_input)
string_len = len(user_input)

match_count = 0

if string_len == 0:
    match_count = input_len + 1
else:
    index = 0

    while index <= input_len - string_len:
        current_slice = user_input[index : index + string_len]
