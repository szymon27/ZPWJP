import requests
import json
import argparse
from Brawery import Brawery


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--city')
    args = parser.parse_args()
    cityFilter = ''
    if args.city is not None:
        cityFilter = f'by_city={args.city}&'

    url = f'https://api.openbrewerydb.org/v1/breweries?{cityFilter}page=1&per_page=20'
    response = requests.get(url)
    braweries = json.loads(response.content)

    for i in range(len(braweries)):
        temp = braweries[i]
        braweries[i] = Brawery(**temp)

    for item in braweries:
        print(item)
