months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]



date = input("Date: ")
while True:
    try:
    elements = date.split("/")
    if len(elements[1]) ==1:
        elements[1] = "0" + elements[1]
    if  len(elements[0]) ==1:
        elements[0] ="0" + elements[0]
    print(f"{elements[2]}-{elements[0]}-{elements[1]} ")
    except:
        new_date = date.replace(",", "")
        elements = new_date.split(" ")
        if elements[0] in months and :
            if len(elements[1]) ==1:
                elements[1] = "0" + elements[1]

    print(f"{elements[2]}-{months.index(elements[0])}-{elements[1]} ")
    else:
        pass




