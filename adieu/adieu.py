
names = []
while True:
    try:
        name = input('Name: ')
        names.append(name)
    except KeyboardInterrupt:
        print(names[:-2])
        for x in names[:-1]:
            print(f'Adieu, Adieu, to {x + ','} and {names[-1]}')
            break
    except EOFError:
        exit(0)

