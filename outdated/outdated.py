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

days_monts = list(range(1,32))

def convert_date(s):
    try:
        date = s.replace(",","")
        new_date = date.split(" ")
        if new_date[0] in months and new_date[1] in days_monts:
            




