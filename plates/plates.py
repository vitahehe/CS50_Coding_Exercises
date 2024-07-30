def main():

    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s.isalnum() or len(s) != 0:
        return True
    if len(s) < 2 or not s[:2].isalpha():
        return False

    # Check for digits only after letters and ensure the first number is not 0
    found_digit = False
    for i, char in enumerate(s):
        if char.isdigit():
            if not found_digit:
                # First digit found
                if char == '0':
                    return False
                found_digit = True
            elif found_digit:
                # Ensure digits are only at the end
                if i < len(s) - 1 and not s[i+1].isdigit():
                    return False

    return True




main()
