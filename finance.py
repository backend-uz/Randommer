import requests
from randommer import Randommer

class Finance(Randommer):
    def get_crypto_address_types(self, api_key: str) -> list:
        '''get available crypto types

        Args:
            api_key (str): api key

        Returns:
            list: list of types
        '''
        headers = {"X-Api-Key":api_key}
        r = requests.get(f'{self.get_url()}Finance/CryptoAddress/Types', headers=headers)
        return r.json()

    def get_crypto_address(self, crypto_type: str, api_key: str) -> dict:
        '''get available crypto address

        Args:
            crypto_type (str): crypto type
            api_key (str): api key

        Returns:
            dict: crypto address
        '''
        headers = {"X-Api-Key":api_key}
        payload = {"cryptoType":crypto_type}
        r = requests.get(f'{self.get_url()}Finance/CryptoAddress/',params=payload, headers=headers)
        return r.json()

    def get_countries(self, api_key: str) -> list:
        '''get available countries

        Args:
            api_key (str): api key

        Returns:
            list: crypto address
        '''
        headers = {"X-Api-Key":api_key}
        r = requests.get(f'{self.get_url()}Finance/Countries', headers=headers)
        return r.json()

    def get_iban_by_country_code(self, country_code: str, api_key: str) -> dict:
        '''get available countries

        Args:
            country_code (str): country code
            api_key (str): api key

        Returns:
            dict: idan data
        '''
        headers = {"X-Api-Key":api_key}
        r = requests.get(f'{self.get_url()}Finance/Iban/{country_code}', headers=headers)
        return r.json()
fin = Finance()
key = "689160d3ed5c445a8ddf7b1820957a75"
print(fin.get_iban_by_country_code("AL", key))