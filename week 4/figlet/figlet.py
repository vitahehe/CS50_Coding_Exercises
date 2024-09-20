import pyfiglet
import sys
import random

if len(sys.argv) ==2:
    sys.exit('Invalid usage')

elif len(sys.argv) == 1:
    imput = input('Input: ')
    available_fonts = pyfiglet.FigletFont.getFonts()
    random_font = random.choice(available_fonts)
    results = pyfiglet.figlet_format(f'{imput}', font =random_font)
    print(results)

elif len(sys.argv) == 3:
    available_fonts = pyfiglet.FigletFont.getFonts()
    if (sys.argv[1] == '-f' or sys.argv[1] == '--font') and sys.argv[2] in available_fonts:
        imput = input('Input: ')
        results = pyfiglet.figlet_format(f'{imput}' , font = sys.argv[2])
        print(results)
    else:
        sys.exit('Invalid usage')
else:
    sys.exit('Invalid usage')


