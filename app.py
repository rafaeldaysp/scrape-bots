import requests
import json
import concurrent.futures
import acer_scrape, magalu_scrape, amazon_scrape, aliexpress_scrape #incluir os demais varejistas
import time

API_KEY = 'UfLk014eu5loeUzkBWi67ku9s2FGdNuFTmxcysQGO7BZS0NfIQQyCXpQ1GzAHDUHfQKTJDnAIBSQAOmYbnnczuoe5ys8maufkBpk73kbqGzeWYD9qGysLXidBMzWeDnN'
MAIN_URL = 'http://localhost:3333'
RETAILERS_ID = {'ACER': 'd85b304d-b19a-4717-a3bd-88553d1bb0d4',
                'AMAZON': '57ad8275-bd9a-4ea7-9a5d-e5ff76760900',
                'ALIEXPRESS': 'c301b951-1dc7-47e6-b51f-d6da74b4f1cf',
                'CASAS BAHIA': '',
                'KABUM': '',
                'CARREFOUR': '',
                'MAGALU': ''}

def coupon_handle(price, store, retailer, product):
    retailer_id = retailer['id']
    try:
        category = product['category']['name']
    except:
        category = ''
    discount_amount = 0
    best_coupon_id = None
    coupons = json.loads(requests.get(MAIN_URL + '/coupons', headers={'api-key': API_KEY}).text) 
    for coupon in coupons:
        if not coupon['minimum_spend']:
            coupon['minimum_spend'] = 0
        if not coupon['store']:
            coupon['store'] = ''
        if not coupon['description']:
            coupon['store'] = ['']
        if coupon['retailer']['id'] == retailer_id and coupon['minimum_spend'] <= price and coupon['store'] in store \
            and coupon['available'] and category in coupon['description']: #incluir condição de categoria (Kabum)
            discount = coupon['discount']
            if '%' in discount:
                discount = float(discount[:-1])*price/100
            else:
                discount = float(discount)
            if discount > discount_amount:
                best_coupon_id = coupon['id']
                discount_amount = discount
    return [best_coupon_id, discount_amount]

def scraping(product):
    product_id = product['id']
    retailers = json.loads(requests.get(MAIN_URL + '/products/' + product_id + '/retailers', headers={'api-key': API_KEY}).text)
    for retailer in retailers:
        data = {}
        retailer_id = retailer['retailer']['id']
        url = retailer['html_url']
        if retailer_id == RETAILERS_ID['ACER']:
            price, store = acer_scrape.scrape(url)
        if retailer_id == RETAILERS_ID['ALIEXPRESS']:
            price, store = aliexpress_scrape.scrape(url, retailer['dummy'])
        if retailer_id == RETAILERS_ID['AMAZON']:
            price, store = amazon_scrape.scrape(url)
        if price != -1:
            coupon_data = coupon_handle(price, store, retailer, product)
            data['available'] = True
            data['coupon_id'] = coupon_data[0]
            data['price'] = int((price - coupon_data[1])*100)
            data['store'] = store
        else:
            data['available'] = False
            print('erro')
        print(product['title'], data)
        r = requests.patch(MAIN_URL + '/products/' + product_id + '/retailers/' + retailer_id, json=data, headers={'api-key': API_KEY})
            

def main():
    while True:
        products = json.loads(requests.get(MAIN_URL + '/products', headers={'api-key': API_KEY}).text)
        concurrent.futures.ThreadPoolExecutor().map(scraping, products)
        time.sleep(5)

if __name__ == '__main__':
    main()