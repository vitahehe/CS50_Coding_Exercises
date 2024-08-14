import pyfiglet
import sys

try:
    imput = input('Input: ')
    if len(sys.argv) == 0 or len(sys.argv) == 2:
        if len(sys.argv) == 0:
            results = pyfiglet.figlet_format(sys.a, font = 'random')
            print(results)
        elif len(sys.argv) == 2:
            results = pyfiglet.figlet_format(sys.a, font = 'random')



except ValueError:
    sys.exit()
