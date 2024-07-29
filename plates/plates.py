def main():

    plate = input("Plate: ")
    plate_char = [char for char in plate]
    print(plate_char)
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= s <= 6:
        return True
    def is_alphanumeric(s):
        return s.isalnum() and len(s)> 0 




main()
