camelcase = input("whats the name of a variable?")

for capital in camelcase:
    if capital.isupper:
        return camelcase.split()


