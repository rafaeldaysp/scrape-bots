import requests
import json
from assignments import API_KEY, MAIN_URL

headers = {'api-key': API_KEY}

def get_coupons(retailer_id):
    return json.loads(requests.get(MAIN_URL + '/retailers/' + retailer_id + '/coupons', headers=headers).text)

def get_product_retailers(product_id):
   return json.loads(requests.get(MAIN_URL + '/products/' + product_id + '/retailers', headers=headers).text)

def update_product_retailers(product_id, retailer_id, data):
    return requests.patch(MAIN_URL + '/products/' + product_id + '/retailers/' + retailer_id, json=data, headers=headers)

def get_products():
    return json.loads(requests.get(MAIN_URL + '/products', headers=headers).text)

def get_coupon(coupon_id):
    return json.loads(requests.get(MAIN_URL + '/coupons/' + coupon_id, headers=headers).text)