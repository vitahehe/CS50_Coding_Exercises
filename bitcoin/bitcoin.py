import sys
import requests
try:
    try:
        if len(sys.argv) == 1:
            sys.exit('Missing command-line argument ')
        bit= float(sys.argv[1])
    except ValueError:
        sys.exit('Command-line argument is not a number')

    url = f'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    bit_usd = data['bpi']['USD']['rate']
    print(f'${bit_usd}')

except requests.RequestException as e:
    print(f'An error {e} has occured')




