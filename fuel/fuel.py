

def get_percantage(s):
    while True:
        try:
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
                print(result,"%")
                break

        except ValueError:
            print("a")

        except ZeroDivisionError:
            print("a2")
            
x = get_percantage(input("Fraction: "))


