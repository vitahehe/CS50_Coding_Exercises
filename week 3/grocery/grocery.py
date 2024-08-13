items = []

while True:
    try:
        item = input(" ")
        items.append(item)

    except KeyboardInterrupt:
        dictionary = {}

        capitalized_list = [i.upper() for i in items]
        for x in capitalized_list:
            if x in dictionary:
                dictionary[x] += 1
            else:
                dictionary[x] = 1

        numbers = list(dictionary.values())
        fruits = list(dictionary.keys())

        for item1, item2 in zip(numbers, fruits):
            print(f"{item1} {item2} ")
        break

    except EOFError:
        exit(0)

