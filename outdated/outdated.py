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
            if len(new_date[1]) == 1:
                new_date[1] = "0" + new_date[1]
        month_index = months.index(new_date[0])+1
        month_index_str = f"{month_index:02}"
        print(f"{new_date[2]}-{month_index_str}-{new_date[1]}")
    except ValueError:
        date = s.split("/")
        if len(date[0]) == 1:
            date[0]= "0" + date[0]
        if len(date[1]) == 1:
            date[1] = "0" + date[1]
        print(f"{date[2]}-{date[0]}-{date[1]}")

convert_date(input("Date: "))







