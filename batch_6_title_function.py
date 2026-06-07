user_input = input("Enter text: ")

if user_input == "":
    result = ""

else:
    word_list = user_input.split()

    words_checked = []

    for word in word_list:
        if word == "":
            words_checked.append("")
        
        else:
            first_char = word[0]
            remaining_char = word[1:]

            word_upper = first_char.upper()
            word_lower = remaining_char.lower()

            final_string = word_upper + word_lower

            words_checked.append(final_string)

result = " ".join(words_checked)

print(result)