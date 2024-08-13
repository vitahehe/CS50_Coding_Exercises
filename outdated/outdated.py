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



while True:
    date = input('Date: ')
    try:
        date_list = date.split('/')
        if date_list[1] in days_monts and date_list[0] in dict.keys():
            if len(str(date_list[0])) == 1:
                date_list[0] = '0' + date_list[0]
            if len(str(date_list[1])) == 1:
                date_list[1] = '0' + date_list[1]
            print(f'{date_list[2]}-{date_list[0]}-{date_list[1]}')
            break

    except ValueError:
        date_2 = date.replace(',', '')
        date_22 = date_2.split(' ')
        if date_22[0] in months and date_22[1] in day_monts:
            if len(dict[date_22[0]]) == 1:
                date_22[0] = '0' + date_22[0]
            if len(date_22[1]) == 1:
                date_2[1] = '0' + date_2[1]
        print(f'{date_2[2]}-{date_2[0]}')
        break








