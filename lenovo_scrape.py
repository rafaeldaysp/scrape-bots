from bs4 import BeautifulSoup
from api.scrape_request import get_response

url = 'https://click.linksynergy.com/deeplink?id=HWP*/f3BEF0&mid=47364&murl=https%3A%2F%2Fwww.lenovo.com%2Fbr%2Fpt%2Flaptops%2Fideapad%2Fserie-300%2FIdeaPad-3-15ALC6%2Fp%2F82MFS00000%3F'

def scrape(url, **kwargs):
    price = -2
    site = BeautifulSoup(get_response(url).content, 'html.parser')
    try:
        price = float(site.find('dd', {'itemprop': 'price'}).text[3:].replace('.', '').replace(',', '.'))
        stock_msg = site.find('span', {'class': 'stock_message'}).text
        if stock_msg == 'Esgotado':
            price = -1
    except:
        price = -2
    return price, 'Lenovo'

if __name__ == '__main__':
    print(scrape(url))