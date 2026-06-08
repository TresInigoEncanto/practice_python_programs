user_input = input("Enter text: ")
string_count = input("Enter substring to count: ")

input_len = len(user_input)
string_len = len(string_count)

match_count = 0

if string_len == 0:
    match_count = input_len + 1
else:
    index = 0

    while index <= input_len - string_len:
        current_slice = user_input[index : index + string_len]

        if current_slice == string_count:
            match_count += 1
            index += string_len
        else:
            index += 1

print(f"{string_count} appears {match_count} times")
