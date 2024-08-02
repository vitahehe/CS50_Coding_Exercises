amount_due = 50
print("Amount Due :", amount_due)

while amount_due != 0 :
    prompt = int(input("Insert Coin: "))
    if prompt == 25 or prompt ==10 or prompt == 5 :
            amount_due = amount_due  - prompt
            print("Amount Due :", amount_due)
    else:
          print("Amount Due: ", amount_due)

print("Change Owed: 0")



