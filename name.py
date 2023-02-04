import requests
from randommer import Randommer


class Name(Randommer):
    def get_name(self, api_key: str, nameType: str, quantity: int) -> list:
        '''get name

        Args:
            api_key (str): api key
            nameType (str): nameType
            quantity (str): number of names

        Returns:
            list: list of names
        '''
        headers = {"X-Api-Key":api_key}
        params = {"nameType": nameType, "quantity":quantity}
        r = requests.get(f'{self.get_url()}Name', headers=headers)
        return r.json()
    
    def get_name_suggestions(self, api_key: str, startingWords: str) -> list:
        '''get name suggestions

        Args:
            api_key (str): api key
            startingWords (str): startingWords

        Returns:
            list: list of name suggestions
        '''
        headers = {"X-Api-Key":api_key}
        params = {"startingWords": startingWords}
        r = requests.get(f'{self.get_url()}Name/Suggestions', params=params, headers=headers)
        return r.json()
    
    def get_name_cultures(self, api_key: str) -> list:
        '''get available cultures

        Args:
            api_key (str): api key

        Returns:
            list: list of names
        '''
        headers = {"X-Api-Key":api_key}
        r = requests.get(f'{self.get_url()}Name/Cultures', headers=headers)
        return r.json()
name = Name()
key = "689160d3ed5c445a8ddf7b1820957a75"
print(name.get_name_cultures(key))