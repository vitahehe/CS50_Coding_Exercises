def main():
    x= get_percantage(input("Fraction:"))

def get_percantage(s):
    while True:
        try:
            fraction_list = s.split("/")
            fraction_list = [int(i) for i in fraction_list]
            result = (fraction_list[0] / fraction_list[1]) * 100
            print(result,"%")
        except ValueError:
            input("Fraction:")
        else:
            break

main()


