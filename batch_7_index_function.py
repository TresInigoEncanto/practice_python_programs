user_input = input("Enter text: ")
string_search = input("Enter substring to find: ")

input_len = len(user_input)
sub_len = len(string_search)

found_index = -1

if sub_len == 0:
    found_index == 0
else:
    for i in range(input_len - sub_len + 1):
        current_slice = user_input[i : i + sub_len]

        if current_slice == string_search:
            found_index = i
            break