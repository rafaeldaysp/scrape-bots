from bs4 import BeautifulSoup
from response_handler import get_response
import json

def scrape(url = 'https://www.carrefour.com.br/tela-140-ibm-lenovo-g4070-series-fosca-mp927338838/p'):
    price, store = [-1, None]
    r = get_response(url)
    script = BeautifulSoup(r.content, 'html.parser').find('script', {'type': 'application/ld+json'})
    try:
        data = json.loads(script.contents[0])
        price = data['offers']['offers'][0]['price']
        store = data['offers']['offers'][0]['seller']['name']
    except:
        pass
    print(price, store)
    
if __name__ == '__main__':
    scrape()