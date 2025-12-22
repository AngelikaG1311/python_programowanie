import requests
from typing import Optional
import argparse

class Brewery:
    def __init__(self,id:str,name:str,brewery_type:str,address_1:Optional[str],address_2:Optional[str],
                 address_3:Optional[str],city:str,state_province:str,postal_code:str,country:str,
                 longtitude:Optional[int],lattitude:Optional[int],phone:Optional[str],website:Optional[str],
                 state:str,street:Optional[str]):
        self.id=id
        self.name=name
        self.brewery_type=brewery_type
        self.address_1=address_1
        self.address_2=address_2
        self.address_3=address_3
        self.city=city
        self.state_province=state_province
        self.postal_code=postal_code
        self.country=country
        self.longtitude=longtitude
        self.lattitude=lattitude
        self.phone=phone
        self.website=website
        self.state=state
        self.street=street
    def __str__(self):
        return(
            f" Brewery: {self.name,}, {self.brewery_type},"
            f" Address: {self.city}, {self.state_province}, {self.postal_code}, {self.country}"
            f" Contact: {self.phone},  {self.website}"
        )

def main():
    parser = argparse.ArgumentParser(description="Pobierz listę browarów z OpenBreweryDB.")
    parser.add_argument("--city", type=str, help="Miasto, z którego chcesz pobrać browary")
    args = parser.parse_args()

    url = "https://api.openbrewerydb.org/v1/breweries?per_page=20"
    if args.city:
        url += f"&by_city={args.city}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    breweries=[]
    for item in data:
        brewery=Brewery(
        id=item.get("id", ""),
        name=item.get("name", ""),
        brewery_type=item.get("brewery_type", ""),
        address_1=item.get("address_1", ""),
        address_2=item.get("address_2", ""),
        address_3=item.get("address_3", ""),
        city=item.get("city", ""),
        state_province=item.get("state_province", ""),
        postal_code=item.get("postal_code", ""),
        country=item.get("country", ""),
        longtitude=item.get("longtitude", ""),
        lattitude=item.get("lattitude", ""),
        phone=item.get("phone", ""),
        website=item.get("website", ""),
        state=item.get("state", ""),
        street=item.get("street", "")
        )
        breweries.append(brewery)

    if breweries:
            for b in breweries:
                print(b)
    else:
            print(f"Nie znaleziono browarów dla miasta: {args.city}")

if __name__ == "__main__":
    main()

