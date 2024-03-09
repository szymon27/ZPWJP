import requests
import json
import argparse

class Brawery:

    def __init__(self,  id: str, name: str, brewery_type: str, address_1: str, address_2: str, address_3: str, city: str, state_province: str, postal_code: str, country: str, longitude: str, latitude: str, phone: str, website_url: str,state: str, street: str):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.address_1 = address_1
        self.address_2 = address_2
        self.address_3 = address_3
        self.city = city
        self.state_province = state_province
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url
        self.state = state
        self.street = street

    id: str
    name: str
    brewery_type: str
    address_1: str
    address_2: str
    address_3: str
    city: str
    state_province: str
    postal_code: str
    country: str
    longitude: str
    latitude: str
    phone: str
    website_url: str
    state: str
    street: str

    def __str__(self):
        return f'Id: {self.id}\nName: {self.name}\nType: {self.brewery_type}\nCity: {self.city}'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--city')
    args = parser.parse_args()
    cityFilter = ''
    if args.city != None:
        cityFilter = f'by_city={args.city}&'

    response = requests.get(f'https://api.openbrewerydb.org/v1/breweries?{cityFilter}page=1&per_page=20')
    braweries = json.loads(response.content)

    for i in range(len(braweries)):
        temp = braweries[i]
        braweries[i] = Brawery(**temp)

    for item in braweries:
        print(item)