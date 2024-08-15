impport sys
import inflect

names = []
while True:
    try:
        name = input('Name: ')
        names.append(name)
    except KeyboardInterrupt:
        sys.exit()


    except EOFError:
        exit(0)

