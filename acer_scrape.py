from bs4 import BeautifulSoup
from api.scrape_request import get_response
import json
from api import api

def coupon_validation(description, product):
    if description:
        try:
            description = json.loads(description)
            if not description['product_id'] in product['id']:
                return False
        except:
            pass
    return True

def scrape(url, **kwargs):
    response = get_response(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    available_status = soup.find('span', class_='b vtex-rich-text-0-x-strong')
    if available_status:
        print('Indisponível')
        return -1, None
    coupons = soup.find_all('div', class_='vtex-flex-layout-0-x-flexColChild vtex-flex-layout-0-x-flexColChild--flagCoupon pb0')
    cupom_value = 0
    i = 0
    for cupom in coupons:
        i += 1
        if cupom.text:
            cupom_value = i*100
            #print('Cupom de {} reais'.format(cupom_value) + ': ' + str(cupom_value) + 'off')
            data = {'code': str(cupom_value) + 'off', 'discount': str(cupom_value), 'retailer_id': kwargs['retailer_id'], 'available': True, 'description': '{"product_id": "'+ kwargs['product_id'] +'"}'}
            coupons = api.create_coupon(data)
    
    precos = soup.find_all('span', class_='vtex-product-price-1-x-currencyContainer vtex-product-price-1-x-currencyContainer--productPage-installments')
    preco = precos[0].text
    preco_value = float(preco[3:].replace('.', '').replace(',', '.'))
    #preco_com_cupom = preco_value - cupom_value ## Na versão final, fazer a comparação entre cupons a partir do banco de dados
    preco_final_pix = preco_value*0.9
    return preco_final_pix, 'Acer'

if __name__ == '__main__':
    scrape('https://br-store.acer.com/notebook-acer-an517-54-56q0-ci511400h-8gb-1tb-256gb-ssd-4g-gddr6-wnhcsl64-black-17-3-fhd-nh-qegal-001/p', retailer_id = '53b2e99e-a8e8-4d59-9305-5907b3b6f283', product_id = 'ba9ed55e-65c4-42eb-9ffb-ab1348102258')