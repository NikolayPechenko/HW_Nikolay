import requests

url = 'https://min-api.cryptocompare.com/data/price'
a = input('Введите валюту 1 : ')
b = input('Введите валюту 2 : ')
c = int(input('Введите количество: '))
response = requests.get(url, params={'fsym': a, 'tsyms': b})
print(response.json()[b] * c)
