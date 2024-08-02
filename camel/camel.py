camelCase = input("camelCase: ")
for char in camelCase:
    snake_case = []
    if char is char.isupper():
        camelCase.replace(char, "_" + char.lower())
