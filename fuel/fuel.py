

def get_percantage():
    while True:
        try:
            s = input("Fraction: ")
            fraction_list = s.split("/")
            fraction_list = [int(i) for i in fraction_list]
            result = (fraction_list[0] / fraction_list[1]) * 100
            if result > 1:
                input("Fraction:")
            if result == 1:
                print("F")
            if result == 0:
                print("E")

            else:
                print(result,"%")

        except ValueError:
            input("Fraction:")

        except ZeroDivisionError:
            input("Fraction:")



