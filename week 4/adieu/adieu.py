import sys
#doesnt work yet
names = []
while True:
    try:
        name = input('Name: ')
        names.append(name)
    except KeyboardInterrupt:
        if len(names) == 0:
            sys.exit()
        elif len(names)==2:
            final_names = names[0] + ' and ' + names[1]
        elif len(names) ==1:
            final_names = names[0]
        else:
            final_names = ', '.join(names[:-1]) + ', and ' + names[-1]
        print(f'Adieu, Adieu, to {final_names}')
        sys.exit(0)



    except EOFError:
        exit(0)

