def main():

    plate = input("Plate: ")
    plate_char = [char for char in plate]
    print(plate_char)
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= plate_char <= 6:
        return "yes"



main()
