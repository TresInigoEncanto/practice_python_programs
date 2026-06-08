user_input = input("Enter text: ")
result = ""

for char in user_input:
    if 'a' <= char <= 'z':
        result += chr(ord(char) - 32)
    else:
        result += char

print(result)
    