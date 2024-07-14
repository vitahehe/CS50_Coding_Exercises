coke = 50
print("Amount Due: ", coke)
payment = int(input("Input Coin: "))

if payment == 50 or payment == 25 or payment == 10 or payment ==5 :
        while coke != 0:
              print("Amount Due: ", coke - payment)
              coke = coke - payment
              if coke != 0:
                    payment = int(input("Input Coin: "))
              else:
                    print("Change Owed: 0")


else:
    print("Amount Due: ", coke)


