text = "hello_people_of_earth"
prefix = "hello_"

without_prefix = text[len(prefix):] if text.startswith(prefix) else text

print(f"Result: {without_prefix}")