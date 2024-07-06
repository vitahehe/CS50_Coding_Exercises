

time = str(input("what time is it?").lower().strip())

def replacesymbol(x ,y , z):
    return x.replace(y,z)
convertedtime = float(replacesymbol(time, ":", "."))
breakfast1 = 07.00
breakfast2 = 08.00
lunch1 = 12.00
lunch2 = 13.00
dinner1 = 18.00
dinner2 = 19.00

if breakfast1 <= convertedtime <= breakfast2 :
        print("breakfast")
elif lunch1 <= convertedtime <= lunch2 :
        print("lunch")
elif dinner1 <= convertedtime <= dinner2:
        print("dinner")

