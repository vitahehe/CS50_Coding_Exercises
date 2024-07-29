def main():

    plate = input("Plate: ")
    plate_char = list(plate)
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= plate_char <= 6:
        return "yes"



main()
