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

dict = {str(i+1): months[i] for i in range(len(months))}

date= input('Date: ')

while True:
    try:
        date_list = date.split('/')
        if date_list[1] in day_monts and date_list[0] in dict.keys():
            if date_list[0] == len(1):
                date_list[0] = '0' + date_list[0]
            if date_list[1] == len(1):
                date_list[1] = '0' + date_list[1]
            print(f'{date_list[2]}-{date_list[0]}-{date_list[1]}')
    except ValueError:
        date_2 = date.split(' ').remove(',')
        if date_2[0] in months and date_2[1] in day_monts:
            if date_2[0] == len(1):
                date_2[0] = '0' + date_2[0]
            if date_2[1] == len(1):
                date_2[1] = '0' + date_2[1]
        print(f'{date_2[2]-{date_2[0]}')








