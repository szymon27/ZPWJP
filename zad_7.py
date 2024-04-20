import requests
import json
from Brawery import Brawery


if __name__ == '__main__':
    url = "https://api.openbrewerydb.org/v1/breweries?page=1&per_page=20"
    response = requests.get(url)
    braweries = json.loads(response.content)

    for i in range(len(braweries)):
        temp = braweries[i]
        braweries[i] = Brawery(**temp)

    for item in braweries:
        print(item)
