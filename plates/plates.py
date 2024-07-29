def main():

    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    found_digit = False
    for char in s:
        if char.isdigit():
            found_digit = True
        elif found_digit:
            return False
    for i, char in enumerate(s):
        if char.isdigit():
            # Check if the first digit is '0'
            if char == '0':
                return False
    return s.isalnum() and len(s)> 0 and s[:2].isalpha() and (2 <= len(list(s)) <= 6)






main()
