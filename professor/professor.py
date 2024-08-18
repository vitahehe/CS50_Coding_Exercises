import random


def main():
    level_l = get_level()
    for i in range(10):
        i = input(f'{generate_integer(level_l)} + {generate_integer(level_l)} = ')
        print(i)


def get_level():
    while True:
        level = int(input('Level: '))
        if level == 1 or level ==2 or level ==3:
            return level
        else:
            continue



def generate_integer(level):
    if not 0 <level< 4:
        raise ValueError
    min_n = 10**(level -1)
    max_n = 10**level - 1
    r_int = random.randint(min_n , max_n)
    return r_int





if __name__ == "__main__":
    main()
