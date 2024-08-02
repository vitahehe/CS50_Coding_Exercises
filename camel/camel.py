camelCase = input("camelCase: ")
snake_case_l =[]
for char in camelCase:
        if char.isupper():
            snake_case_l.append('_')
            snake_case_list.append(char.lower())
        else:
            snake_case_list.append(char)


    snake_case = ''.join(snake_case_l)
    return snake_case
