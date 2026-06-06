text = input("Enter input: ")
result = ""

for char in text:
    if 'A' <= char <= 'Z':
        result += chr(ord(char) + 32)
    else:
        result += char
print(result)           