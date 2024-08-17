import random
import sys

intiger = int(input('Level: '))
while intiger <= 0:
    intiger = int(input('Level: '))
random_intiger = random.randrange(1, intiger)

while True:
    gess = int(input('Guess: '))
    if gess > random_intiger:
        print('Too large!')
        continue
    elif gess < random_intiger:
        print('Too small!')
        continue
    elif gess == random_intiger:
        print('Just right!')
        sys.exit()




