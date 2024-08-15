import sys
import inflect

names = []
while True:
    try:
        name = input('Name: ')
        names.append(name)
    except KeyboardInterrupt:
        for i in range(1,(len(names)*2) -1 , 2):
            names.insert(i, ',')
        names[-2] = 'and'
        result = ' '.join(names)
        print(f'Adieu, Adieu, to {result}')
        sys.exit()


    except EOFError:
        exit(0)

