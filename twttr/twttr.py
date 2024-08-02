def main():
    Input = input("Something:" ).strip().lower()
    Changed_Input= shorten(Input)
    print(Changed_Input)

    def shorten(s):
        vowels ="aeiou"
        result = []
        for char in s:
            if char not in vowels:
                result.append(char)
        return ''.join(result)

main()
