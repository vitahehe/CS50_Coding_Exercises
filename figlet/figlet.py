import pyfiglet
import sys

try:
    imput = input('Input: ')
    if len(sys.argv) == 0 or len(sys.argv) == 2:
        if len(sys.argv) == 0:
            results = pyfiglet.figlet_format(imput, font = 'random')
            print(results)
        elif len(sys.argv) == 2:
            results = pyfiglet.figlet_format(imput , font = sys.argv[2])
            print(results)



except ValueError:
    sys.exit()
