camelCase = input("camelCase: ")
for char in camelCase:
    if char is char.isupper():
        camelCase.replace(char, "_" + char.lower())
