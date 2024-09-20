import sys

try:
    if len(sys.argv) == 1:
        sys.exit('Missing command-line argument ')
    elif sys.argv[1] == float:
        bitcoin = sys.argv[1]
except ValueError:
    sys.exit('Command-line argument is not a number')

print(f'{bitcoin}')
