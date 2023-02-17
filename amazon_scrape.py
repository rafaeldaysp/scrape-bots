from bs4 import BeautifulSoup
from response_handler import get_response

def scrape(url):
    response = get_response(url)
    price = -1
    store = None
    if response.status_code != 200:
        print('Acesso bloqueado pela Amazon' )
    site = BeautifulSoup(response.text, 'html.parser')
    try:
        lista_divs = site.find('div', {'class': 'a-section a-spacing-none aok-align-center'})
        price = lista_divs.find('span', class_='a-offscreen').text
        price = float(price[2:].replace('.', '').replace(',', '.'))
        store = site.find('a', id='sellerProfileTriggerId').text
    except Exception as e:
        print(e)
    return price, store


if __name__ == '__main__':
    pass