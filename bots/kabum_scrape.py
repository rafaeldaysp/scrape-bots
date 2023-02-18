import re
from bs4 import BeautifulSoup
from response_handler import get_response

def scrape(url):
    price = -1
    store = None
    response = get_response(url)
    try:
        site = BeautifulSoup(response.content, 'html.parser')
        price = site.find('h4', class_=re.compile('finalPrice')).text[3:].replace('.', '').replace(',', '.')
        store = site.find('div', class_=re.compile('generalInfo')).find('b').text
    except:
        pass
    print(price, store)
    return price, store

if __name__ == '__main__':
    pass