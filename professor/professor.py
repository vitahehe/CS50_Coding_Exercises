import random


def main():



def get_level():
    while True:
        level = int(input('Level: '))
        if level == 1 or level ==2 or level ==3:
            break
        else:
            continue
    return level



def generate_integer(level):
    if not 0 <level< 4:
        raise ValueError
    random.randint(




if __name__ == "__main__":
    main()
