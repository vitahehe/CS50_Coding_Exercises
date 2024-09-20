import random
import sys

while True:

    try:

        intiger = int(input('Level: '))
        while intiger <= 0:
            intiger = int(input('Level: '))
        random_intiger = random.randrange(1, intiger)
        break
    except ValueError:
        continue


while True:
    try:

        gess = int(input('Guess: '))
        if gess > random_intiger:
            print('Too large!')
            continue
        elif 0 < gess < random_intiger:
            print('Too small!')
            continue
        elif gess == random_intiger:
            print('Just right!')
            sys.exit()
    except ValueError:
        continue





