menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total = 0.0

while True:
    try:
        x= input("Item: ")
        xx = ' '.join(word.capitalize() for word in x.split())
        if xx in menu.keys():
            total = total + menu[xx]
            print(f'${total}')
        else:
            continue

    except KeyboardInterrupt:
        break
    except EOFError:
        exit(0)




