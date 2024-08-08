
x = input("Fraction: ")
try:
    fraction_list = x.split("/")
    fraction_list = [int(i) for i in fraction_list]
    result = (fraction_list[0] / fraction_list[1]) * 100
    print( result ,"%")
    break


