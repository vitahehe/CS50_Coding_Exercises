def main():
    payment = int(input("Input Coin: "))
    coke = 50
    while payment != 0:
        print("Amount Due: ", coke - payment)
        payment = int(input("Input Coin: "))


main()



