amount_due = 50
print("Amount Due :", amount_due)

while amount_due > 0 :
    prompt = int(input("Insert Coin: "))
    if prompt in [5, 10, 25]:
            amount_due = amount_due  - prompt
            print("Amount Due :", amount_due)
    else:
          print("Amount Due: ", amount_due)
while amount_due < 0:
      print("Charge Owed: ", amount_due)
      amount_due = amount_due 



