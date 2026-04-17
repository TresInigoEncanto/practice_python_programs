text = input("Enter a text after five spaces (Ex:     Hello!): ")

index = 0
while index < len(text) and text[index] == " ":
    index += 1

sliced_text = text[index:]

print(sliced_text)