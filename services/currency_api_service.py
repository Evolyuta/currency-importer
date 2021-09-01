import requests


class CurrencyApiService:
    host = 'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/'

    def __init__(self):
        pass

    # Getting all currencies from API
    def get_all_currencies(self):
        return self.__send_get_request('currencies')

    # Getting all currency ratios to other currencies from API
    def get_ratios_for_currency(self, currency_code):
        return self.__send_get_request(f'currencies/{currency_code}')

    # Sending request to API
    def __send_get_request(self, endpoint):
        response = requests.get(self.host + endpoint + '.json')
        data = response.json()
        return data
