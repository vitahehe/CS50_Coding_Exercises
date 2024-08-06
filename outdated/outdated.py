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
try:
    elements = date.split("/")
    print(f"{elements[2]}-{elements[0]}-{elements[1]}")
except:
    new_date = date.replace(",", "")
    elements = new_date.split(" ")
    if elements[0] in months:
        print()
