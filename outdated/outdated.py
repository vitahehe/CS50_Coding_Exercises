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
    if len(elements[1]) ==1 or len(elements[0]) ==1 :
        return "0" + elements[1] or "0" + elements[1]
    
except:
    new_date = date.replace(",", "")
    elements = new_date.split(" ")
    if elements[0] in months:
        print(f"{elements[2]}-{months.index(elements[0])}-{elements[1]} ")
