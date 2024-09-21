def main():
    inp= input()
    inpu= convert(inp)
    print(inpu)


def convert(a):
    aaa= a.replace(':)', '🙂') and a.replace(':(', '🙁')
    return aaa


main()
