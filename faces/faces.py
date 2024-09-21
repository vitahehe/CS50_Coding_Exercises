def main():
    inp= input()
    inpu= convert(inp)
    print(inpu)


def convert(a):
    aaa= a.replace(':)' or ':(', '🙂' or '🙁')
    return aaa

main()
