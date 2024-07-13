def main():
    owed_amount = 50

    while owed_amount != 0:
        payment = int(input("Input Coin: "))
        if payment == 25 or payment == 5:
                 owed_amount = owed_amount - payment
                 print("Amount Due: ", owed_amount)
        else:
              print("enter valid coins")

    print("Change Owed: 0")

main()
