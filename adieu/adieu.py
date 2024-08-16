import sys

names = []
while True:
    try:
        name = input('Name: ')
        names.append(name)
    except KeyboardInterrupt:
        if len(names) == 0:
            sys.exit()
        new_names=[]
        for i in range(names[:-1]):
            new_element = i + ','
            new_names.append(new_element)
        new_names[-1] = names[-1]
        new_names[-2] = 'and'
        print(' '.join(new_names))
        sys.exit()


    except EOFError:
        exit(0)

