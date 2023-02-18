from bs4 import BeautifulSoup
from response_handler import get_response

def scrape(url):
    response = get_response(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    price = soup.find('div', class_= 'p-price').find('strong').text.split(' ')[1][:-1]
    price_value = price.replace('.', '').replace(',', '.')
    print(price_value)

    

if __name__ == '__main__':
    pass