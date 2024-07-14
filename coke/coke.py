def main():
    payed_amount = 0
    coke = 50

    while 0 <= payed_amount < 50 and coke != 0:
        print("Amount Due: ", coke )
        payment = int(input("Insert Coin: "))
        if payment in [50, 25, 10, 5]:
            coke = coke - payment
            payment = payed_amount
        


main()

