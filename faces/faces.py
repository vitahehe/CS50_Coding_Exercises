def main():
    inp= input()
    inpu= convert(inp)
    print(inpu)


def convert(a):
    try:
        aaa= a.replace(':)', '🙂')
    except ':(' in a:
        aaa=a.replace(':(', '🙁')


main()
