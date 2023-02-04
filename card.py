import requests, json
from randommer import Randommer


class Card(Randommer):
    def get_card(self, api_key: str, type=None) -> dict:
        '''get card from randommer
        
        Args:
            api_key (str): api key
            type (str): card type

        Returns:
            dict: card data
        '''
        headers = {"X-Api-Key":api_key}

        r = requests.get(f'{self.get_url()}Card', headers=headers)
        return r.json()

    def get_card_types(self, api_key: str) -> list:
        '''get cars types from randommer

        Args:
            api_key (str): api key
            
        Returns:
            list: list of types
        '''
        headers = {"X-Api-Key":api_key}

        r = requests.get(f'{self.get_url()}Card/types', headers=headers)
        return r.json()

card = Card()
key = "689160d3ed5c445a8ddf7b1820957a75"
print(card.get_card_types(key))