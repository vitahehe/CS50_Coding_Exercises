def shorten(s):
    
        vowels ="aeiouAEIOU"
        result = []
        for char in s:
            if char not in vowels:
                result.append(char)
        return ''.join(result)


def main():
    Input = input("Something:" )
    Changed_Input= shorten(Input)
    print(Changed_Input)


main()
