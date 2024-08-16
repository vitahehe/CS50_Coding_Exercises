import sys
import inflect

names = []
while True:
    try:
        name = input('Name: ')
        names.append(name)
    except KeyboardInterrupt:
        if len(names) == 0:
            sys.exit()
        for i in range(len(names[:-1])):
            

        names[-2] = 'and'
        print(f'Adieu, Adieu, to {result}')
        sys.exit()


    except EOFError:
        exit(0)

