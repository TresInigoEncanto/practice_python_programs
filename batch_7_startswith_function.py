user_input = input("Enter text: ")
find_prefix = input("Enter prefix to check: ")

text_len = len(user_input)
prefix_len = len(find_prefix)

starts_with_prefix = True

if prefix_len > text_len:
    starts_with_prefix = False

else:
    for i in range(prefix_len):
        text_char = user_input[i]
        prefix_char = find_prefix[i]

        if text_char != prefix_char:
            starts_with_prefix = False

print(f"Starts with prefix? {starts_with_prefix}")