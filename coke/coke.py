def main():
    payed_amount = 0
    coke = 50
    while payed_amount < 50:
        print("Amount Due: ", coke )
        payment = int(input("Insert Coin: "))
        if payment in [50, 25, 10, 5]:
            payed_amount = payment
            print("Amount Due: ", coke - payed_amount)
        else:
            print("Amount Due: ", coke)


