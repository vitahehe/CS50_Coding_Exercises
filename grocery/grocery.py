def main():
    list = []
    while True:
        try:
            item = input("Item: ")
            list.append[item]
        except KeyboardInterrupt:
            make_grolist(list)



def make_grolist(s):
    dictionary ={}
    capitalized_list = [i.upper() for )in s]
    for x in capitalized_list:
        if x in dictionary:
            dictionary[x] += 1
        else:
            dictionary[x] = 1
    print(f"{dictionary.keys()} {dictionary.values()}")

main()


