coke = 50
print("Amount Due: ", coke)
payment = int(input("Input Coin: "))

if payment == 50 or payment == 25 or payment == 10 or payment ==5 :
        while payment != 0:
              print("Amount Due: ", coke - payment)
              coke = coke - payment
              payment = 



else:
    print("Amount Due: ", coke)


