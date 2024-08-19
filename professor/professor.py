import random


def main():
    level_l = get_level()
    total = []
    for question in range(10):
        x =generate_integer(level_l)
        y = generate_integer(level_l)
        question = str(x) + ' + ' +  str(y)
        answer = x + y

        for i in range(3):
            try:
                user_q= int(input(f'{question} = '))

                if user_q == answer:
                     total.append(1)
                     break
                if i == 2:
                     total.append(0)
                     print(answer)
                elif user_q != answer:
                     print('EEE')
            except ValueError:
                if i == 2:
                     total.append(0)
                     print(answer)
                else:
                     print('EEE')
    print(f'Score: {sum(total)}')



def get_level():
    while True:
        level = int(input('Level: '))
        if level == 1 or level ==2 or level ==3:
             return level
        elif 
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
