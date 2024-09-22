def main():
    inp= input()
    inpu= convert(inp)
    print(inpu)


def convert(a):
    if ':(' in a:
        a= a.replace(':(','🙁')
    if ':)' in a:
        a= a.replace(':)', '🙂')
    else:
        a =a
    return a


main()
