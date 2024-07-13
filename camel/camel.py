camelcase = list(input("whats the name of a variable?"))

for letter in camelcase:
    if letter.isupper():
        separator = str(letter)
camelcases = str(camelcase).split(separator)

print(camelcases[0], "_", camelcases[1])


