amount_due = 50

while amount_due > 0 :
    print("Amount Due :", amount_due)
    prompt = int(input("Insert Coin: "))
    if prompt in [5, 10, 25]:
            amount_due -= prompt
    else:
          print("Amount Due: ", amount_due)
if amount_due < 0:
    print("Change Owed:", -amount_due)
elif amount_due == 0:
    print("No change owed.")



