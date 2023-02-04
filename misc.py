import requests
from randommer import Randommer


class Misc(Randommer):
    def get_cultures(self, api_key: str) -> list:
        '''get available misc cultures

        Args:
            api_key (str): api key

        Returns:
            list: list of cultures
        '''
        headers = {"X-Api-Key":api_key}
        r = requests.get(f'{self.get_url()}Misc/Cultures', headers=headers)
        return r.json()
    
    def get_random_address(self, api_key: str, number: int, culture='en') -> list:
        '''get available misc cultures

        Args:
            api_key (str): api key
            number (str): number
            culture (str): culture

        Returns:
            list: random address
        '''
        headers = {"X-Api-Key":api_key}
        params = {"number": number, "culture": "en"}
        r = requests.get(f'{self.get_url()}Misc/Random-Address', params=params, headers=headers)
        return r.json()

misc = Misc()
key = "689160d3ed5c445a8ddf7b1820957a75"
print(misc.get_random_address(key, 3))