def main():
    owed_amount = 50

    while owed_amount != 0:
        payment = int(input("Input Coin: "))
        if payment == 25 or payment == 5 or payment == 10 or payment == 50:
                 owed_amount = owed_amount - payment
                 print("Amount Due: ", owed_amount)
        else:
             print("Amount Due: ", owed_amount)

    print("Change Owed: 0")

main()
