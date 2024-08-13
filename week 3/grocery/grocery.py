
list = []
while True:
    try:
        item = input(" ")
        list.append(item)

    except KeyboardInterrupt:
        dictionary ={}
        capitalized_list = [i.upper() for i in list]
        for x in capitalized_list:
            if x in dictionary:
                dictionary[x] += 1
            else:
                dictionary[x] = 1
        numbers = list(dictionary.values())
        fruts = list(dictionary.keys())
        
        break

    except EOFError:
        exit(0)


