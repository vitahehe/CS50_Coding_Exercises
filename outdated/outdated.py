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

days_monts = [str(i) for i in range(1,32)]

date= input('Date: ')

while True:
    try:
        date_list = date.split('/')
        if date_list[1] in day_monts and date_list[0] in months.index







