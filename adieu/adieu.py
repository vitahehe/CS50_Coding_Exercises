
names = []
while True:
    try:
        name = input('Name: ')
        names.append(name)
    except KeyboardInterrupt:
        print(names[:-2])
        for x in names[:-2]:
            print(f'Adieu, Adieu, to {x + ','}')

    except EOFError:
        exit(0)

