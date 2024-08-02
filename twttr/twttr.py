def main():
    Input = input("Something:" ).strip().lower()
    Changed_Input= shorten(Input)
    print(Changed_Input)

    def shorten(s):
        for char in s:
            if char == "a" or char =="e" or char == "i" or char =="o"  or char =="u":
                remove char

