# model.py
# deals with app data and API calls
import requests

url_host = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.min.json"
response = requests.get(url_host)
currency_code_map = response.json()

def get_currencies():
    currency_strings = []
    for code in currency_code_map.keys():
        currency = currency_code_map[code]
        currency_strings.append(code + " - " + currency)
    return currency_strings

def get_currency_from_code(code):
    return currency_code_map[code]

def get_currency_string(code):
    return code + " - " + get_currency_from_code(code)

# API call functions


currencies = get_currencies()
default_from = get_currency_string("usd")
default_to = get_currency_string("eur")

if __name__ == "__main__":
    get_currencies()
    print(url_host)