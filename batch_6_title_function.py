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