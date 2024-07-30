def main():

    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s.isalnum() and len(s) != 0 and s[:2].is alpha() and (2 <= len(s) <= 6):
        return True




main()
