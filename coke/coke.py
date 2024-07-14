def main():
    payed_amount = 0
    coke = 50
    while 0 <= payed_amount < 50:
        print("Amount Due: ", coke )
        payment = int(input("Insert Coin: "))
        if payment in [50, 25, 10, 5]:
            coke = coke - payment
            payed_amount = payment
    print("Change Owed: 0")

main()

