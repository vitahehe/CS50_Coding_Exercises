def main():
    inp= input()
    inpu= convert(inp)
    print(inpu)


def convert(a):
    if ':(' in a:
        aaa= a.replace(':(','🙁')
    elif ':)' in a:
        aaa= a.replace(':)', '🙂')
    else:
        aaa =a
    return aaa


main()
