user_input = input("Enter text: ")
suffix_remove = input("Enter suffix to remove: ")

suffix_len = len(suffix_remove)

if suffix_len > 0 and user_input[-suffix_len:] == suffix_remove:
    removed_suffix = user_input[:-suffix_len]
else:
    removed_suffix = user_input

print(removed_suffix)