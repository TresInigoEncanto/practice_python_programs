full_name = input("Enter your full name using incorrect casing (Ex: TrEs EnCaNtO): ")
snake_case = full_name.lower().replace(" ", "_")

print(snake_case)