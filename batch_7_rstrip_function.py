user_input = input("Enter text: ")
end_index = 0

for i in range(len(user_input) - 1, -1, -1):
    if user_input[i] != " ":
        end_index = i + 1
        break

print(user_input[:end_index])
