

def get_percantage():
    while True:
        try:
            s = input("Fraction: ")
            fraction_list = s.split("/")
            fraction_list = [int(i) for i in fraction_list]
            result = (fraction_list[0] / fraction_list[1]) * 100
            if result >= 100:
                print("F")
                break
            elif result <= 0:
                print("E")
                break
            else:
                print(f"{result}%")
                break

        except ValueError:
            pass

        except ZeroDivisionError:
            pass
get_percantage()


