import sys
import 
try:
    if len(sys.argv) == 1:
        sys.exit('Missing command-line argument ')
    bit= float(sys.argv[1])
except ValueError:
    sys.exit('Command-line argument is not a number')

print(f'{bit}')
