camelCase = input("camelCase: ")
snake_case_l
for char in camelCase:
        if char.isupper():
            if snake_case_list:
                snake_case_l.append('_')
            snake_case_list.append(char.lower())
        else:
            # Otherwise, just append the character
            snake_case_list.append(char)

    # Join the list into a single string
    snake_case_string = ''.join(snake_case_list)
    return snake_case_string
