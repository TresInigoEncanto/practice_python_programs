user_input = input("Enter text: ")

has_lowercase = False
is_all_lowercase = True

for char in user_input:
    if 'A' <= char <= 'Z':
        is_all_lowercase = False
        break

    elif 'a' <= char <= 'z':
        has_lowercase = True