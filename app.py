import concurrent.futures
from api import api
import time
from assignments import RETAILERS_FUNC
from selenium import webdriver
from chrome_options import service, chrome_options

def start(product):
    retailers = api.get_product_retailers(product['id'])
    for retailer in retailers:
        data = {}
        scrape = RETAILERS_FUNC[retailer['retailer']['id']]['scrape_func']
        coupon_validation = RETAILERS_FUNC[retailer['retailer']['id']]['coupon_validation_func']
        price, store = scrape(retailer['html_url'], retailer['dummy'])
        if price > 0:
            data['available'] = True
            data['price'] = int(price*100)
            data['store'] = store
            all_coupons = api.get_coupons(retailer['retailer']['id'])
            possible_coupons = []
            for i in range(len(all_coupons)):
                if coupon_validation(all_coupons[i]['description'], product):
                        possible_coupons.append(all_coupons[i])
            best_discount_amount = 0
            best_coupon_id = None
            for coupon in possible_coupons:
                if not coupon['minimum_spend']:
                    coupon['minimum_spend'] = 0
                if not coupon['store']:
                    coupon['store'] = ''
                if coupon['retailer_id'] == retailer['retailer']['id'] and coupon['minimum_spend'] <= price and coupon['store'] in store and coupon['available']:
                    discount = coupon['discount']
                    if '%' in discount:
                        discount = float(discount[:-1])*price/100
                    else:
                        discount = float(discount)
                    if discount > best_discount_amount:
                        best_coupon_id = coupon['id']
                        best_discount_amount = discount
            data['coupon_id'] = best_coupon_id
            data['price'] = int((price - best_discount_amount)*100)
        elif price == -1:
            data['available'] = False
        response = api.update_product_retailers(product['id'], retailer['retailer']['id'], data)
        print(product['title'], data, response.status_code)

def main():
    products = api.get_products()
    browser = webdriver.Chrome(service=service, options=chrome_options)
    concurrent.futures.ProcessPoolExecutor().map(start, products)

if __name__ == '__main__':
    main()