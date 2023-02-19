from bs4 import BeautifulSoup
from api.scrape_request import get_response

def coupon_validation(description, product):
    return True

def scrape(url, params = None):
    response = get_response(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    available_status = soup.find('span', class_='b vtex-rich-text-0-x-strong')
    if available_status:
        print('Indisponível')
        return -1, None
    coupons = soup.find_all('div', class_='vtex-flex-layout-0-x-flexColChild vtex-flex-layout-0-x-flexColChild--flagCoupon pb0')
    cupom_value = 0
    for i in range(len(coupons)):
        cupom = coupons[i].text
        if cupom:
            cupom_value = (i + 1)*100
            print('Cupom de {} reais'.format(cupom_value) + ': ' + str(cupom_value) + 'off')
    
    precos = soup.find_all('span', class_='vtex-product-price-1-x-currencyContainer vtex-product-price-1-x-currencyContainer--productPage-installments')
    preco = precos[0].text
    preco_value = float(preco[3:].replace('.', '').replace(',', '.'))
    preco_com_cupom = preco_value - cupom_value ## Na versão final, fazer a comparação entre cupons a partir do banco de dados
    preco_final_pix = preco_com_cupom*0.9
    return preco_final_pix, 'Acer'