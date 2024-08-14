import pyfiglet
import sys
import random

imput = input('Input: ')

available_fonts = pyfiglet.FigletFont.getFonts()
random_font = random.choice(available_fonts)

if len(sys.argv) == 0 or len(sys.argv) == 2:
    if len(sys.argv) == 0:
        results = pyfiglet.figlet_format(f'{imput}', font =random_font)
        print(results)
    elif len(sys.argv) == 2:
        results = pyfiglet.figlet_format(f'{imput}' , font = sys.argv[2])
        print(results)


