user_input = input("Enter string: ")
find_suffix = input("Enter suffix to check: ")

text_len = len(user_input)
suffix_len = len(find_suffix)

ends_with_suffix = True

if suffix_len > text_len:
    ends_with_suffix = False

else:
    for i in range(suffix_len):
        text_char = user_input[text_len - 1 - i]
        suffix_char = find_suffix[suffix_len - 1 - i]

        if text_char != suffix_char:
            ends_with_suffix = False
            break

print(f"End with suffix? {ends_with_suffix}")


