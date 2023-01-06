from bs4 import BeautifulSoup
import requests


def get_currency(in_currency, out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    print(f'getting {url}...')
    content = requests.get(url).text
    print(f'parsing content...')
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find('span', class_='ccOutputRslt').get_text()
    rate = float(rate[:-4])
    print(f'returning rate: {rate}')
    return rate


if __name__ == '__main__':
    print(get_currency('USD', 'EUR'))
