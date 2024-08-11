def main():
    list = []
    while True:
        try:
            item = input("Item: ")
            list.append(item)
        except KeyboardInterrupt:
            make_grolist(list)
            break



def make_grolist(s):
    dictionary ={}
    capitalized_list = [i.upper() for i in s]
    for x in capitalized_list:
        if x in dictionary:
            dictionary[x] += 1
        else:
            dictionary[x] = 1
    for keys, values in dictionary.items():
        print(f"{values} {keys}")

main()


