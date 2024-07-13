camelcase = list(input("whats the name of a variable?"))

for letter in camelcase:
    if letter.isupper():
        separator = str(letter)
camelcases = str(camelcase).split(separator)


