def main():
    owed_amount = 50

    while owed_amount != 0:
        payment = int(input("Input Coin: "))
        owed_amount = owed_amount - payment
        print("Amount Due: ", owed_amount)
    print("Change Owed: 0")

main()
