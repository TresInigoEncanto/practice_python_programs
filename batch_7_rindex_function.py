user_input = input("Enter text: ")
string_search = input("Enter substring to find from the right: ")

input_len = len(user_input)
sub_len = len(string_search)

found_index = -1

if sub_len == 0:
    found_index = input_len
else:
    start_search = input_len - sub_len

    for i in range(start_search, -1, -1):
        current_slice = user_input[i: i + sub_len]