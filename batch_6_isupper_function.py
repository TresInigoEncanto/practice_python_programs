text = input("Enter input: ")

has_letter = False
has_lowercase = False

for char in text:
    if 'a' <= char <= 'z':
        has_lowercase = True
        break

    if 'A' <= char <= 'Z':
        has_letter = True

if has_letter and not has_lowercase:
    is_upper_result = True
else:
    is_upper_result = False

print(is_upper_result)
