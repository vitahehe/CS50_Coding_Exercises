def main():
    payment = int(input("Input Coin: "))
    coke = 50
    if payment == 50 or payment == 25 or payment == 10 or payment == 5:
        while payment != 0:
            print("Amount Due: ", coke - payment)
            payment = int(input("Input Coin: "))



main()



