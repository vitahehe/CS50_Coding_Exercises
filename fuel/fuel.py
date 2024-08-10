while True:

    try:
        x = input("Fraction: ")
        fraction_list = x.split("/")
        fraction_list_int = [int(i) for i in fraction_list]
        result = (fraction_list_int[0] / fraction_list_int[1])* 100
        if result == 100 or result == 99:
            print("F")
            break
        elif result > 100:
            continue
        elif result == 0 or result == 1:
            print("E")
            break
        elif result < 0:
            continue
        else:
            print(f'{int(result)}%')
            break

    except ZeroDivisionError:
        continue

    except ValueError:
        continue

