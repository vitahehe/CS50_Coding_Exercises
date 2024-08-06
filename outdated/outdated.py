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
    if elements
except:
    new_date = date.replace(",", "")
    elements = new_date.split(" ")
    if elements[0] in months:
        print(f"{elements[2]}-{months.index(elements[0])}-{elements[1]} ")
