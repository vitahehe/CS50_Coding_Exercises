camelCase = input("camelCase: ")
for char in camelCase:
    if char is char.isupper():

        print(camelCase.replace(char, "_" + char.lower()))
