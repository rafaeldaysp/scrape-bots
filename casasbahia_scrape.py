from bs4 import BeautifulSoup
from response_handler import get_response

def main():
    url = 'https://tidd.ly/3RAzKeV'
    response = get_response(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    price = soup.find('span', class_= 'product-price-value')
    print(price.text)

if __name__ == '__main__':
    main()