
names = []
while True:
    try:
        name = input('Name: ')
        names.append(name)
    except KeyboardInterrupt:
        
    except EOFError:
        exit(0)

