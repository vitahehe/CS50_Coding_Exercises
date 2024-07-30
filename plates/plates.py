def main():

    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s.isalnum() and len(s) != 0 and s[:2].isalpha() and (2 <= len(s) <= 6):
        return True
    found_digit = False
    for char in s:
        if char.isdigit():
            found_digit = True
        elif char.isalpha() and found_digit:
            return False
    return True






main()
