def main():

    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s.isalnum() and len(s) != 0 and s[:2].isalpha() and (2 <= len(s) <= 6):
        return True
    for char in s:
        if s[char].isdigit() and s[char + 1].isaplha():
            return False
        else:
            return True






main()
