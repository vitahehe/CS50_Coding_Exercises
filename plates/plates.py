def main():

    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not  (s.isalnum() and len(s) != 0 and s[:2].isalpha() and (2 <= len(s) <= 6)):
        return False
    for i in range(len(s) - 1):
        if s[i].isdigit() and s[i + 1].isalpha():
            return False
    return True





main()
