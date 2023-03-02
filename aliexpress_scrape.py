import json
import re
import requests
from fake_useragent import UserAgent

def get_response(url):
    ua = str(UserAgent().chrome)
    headers = {'User-Agent': ua}
    r = requests.get(url, headers=headers)
    return r

def coupon_validation(description, product):
    return True

def scrape(url, sku_id):
    price = -1
    retalier = None
    try:
        r = get_response(url)
        match = re.search(r'data: ({.+})', r.text).group(1)
        data = json.loads(match)
        retalier = data['storeModule']['storeName']
        price_info = data['skuModule']['skuPriceList']
        qtd_produtos = len(price_info)
        for i in range(0, qtd_produtos):
            if str(price_info[i]['skuId']) == sku_id:
                if price_info[i]['skuVal']['availQuantity'] == 0:
                    return -1, retalier
                price = price_info[i]['skuVal']['skuActivityAmount']['formatedAmount']
        price_float_value = float(price[3:].replace('.', '').replace(',', '.'))
        try:
            slogan_banner = data['middleBannerModule']['uniformMiddleBanner']['sloganBanner']
            if slogan_banner == 'Preço exclusivo na primeira compra':
                price_float_value += 20
            ## colocar aqui quando tiver desconto de 15 a cada 150 
        except: 
            pass
        
        promo_desc = 0
        try:
            promo_15_off_a_cada = data['couponModule']['webCouponInfo']['promotionPanelDTO']['acrossStoreFixedDiscount'][0]['promotionPanelDetailDTOList'][0]['promotionDesc'].replace('(', '').replace(')', '')
            values_promo = [int(s) for s in promo_15_off_a_cada.split() if s.isdigit()]
            promo_desc = int(price_float_value/values_promo[1])*values_promo[0]
            if promo_desc > values_promo[2]:
                promo_desc = values_promo[2]
        except:
            pass
        price_float_value -= promo_desc
        
        coupons = []
        coupons_conditions = []
       
        try:
            all_coupons = data['couponModule']['webCouponInfo']['promotionPanelDTO']['shopCoupon'][0]['promotionPanelDetailDTOList']
            for coupon_info in all_coupons:
                coupon_value = float(coupon_info['promotionDesc'][3:].replace(',', '.'))
                coupon_condition_str = coupon_info['promotionDetail']
                index = coupon_condition_str.find('$')
                coupon_condition_value = float(coupon_condition_str[index + 2:].replace(',', '.'))
                coupons.append(coupon_value)
                coupons_conditions.append(coupon_condition_value)
            coupons.sort()
            coupons_conditions.sort()
        except:
            pass
        shop_discounts = []
        shop_discounts_conditions = []
        shop_percent_discount_off = 0
        try:
            all_discounts_list = data['couponModule']['webCouponInfo']['promotionPanelDTO']['storeDiscount'][0]['promotionPanelDetailDTOList']
            for i in range(len(all_discounts_list)):
                all_discounts = all_discounts_list[i]['promotionDetailList']
                if 'Tenha' in all_discounts[0]:
                    for discount in all_discounts:
                        shop_discounts.append(float(discount[discount.find('$') + 2:discount.find(',') + 3].replace('.', '').replace(',', '.')))
                        shop_discounts_conditions.append(float(discount[discount.rfind('$') + 2: discount.rfind(',') + 3].replace('.', '').replace(',', '.')))
                if 'Compre 1 ' in all_discounts[0]:
                    percent_value = [float(x) for x in all_discounts[0][all_discounts[0].find('1') + 1:all_discounts[0].find('%')].split(' ') if x.isdigit()][0]
                    shop_percent_discount_off = round(price_float_value*percent_value/100, 2)
                    print(shop_percent_discount_off)
            shop_discounts.sort()
            shop_discounts_conditions.sort()
        except Exception as e:
            pass
        price_float_value -= shop_percent_discount_off    
        shop_discount_off = 0
        for i in range(len(shop_discounts)):
            try:
                if price_float_value > shop_discounts_conditions[i]:
                    shop_discount_off = shop_discounts[i]
            except Exception as e:
                pass
        price_float_value -= shop_discount_off 
        shop_coupon_off = 0
        for i in range(len(coupons)):
            try:
                if price_float_value > coupons_conditions[i]:
                    shop_coupon_off = coupons[i]
            except Exception as e:
                pass
        price_float_value -= shop_coupon_off
        coins_off = 0
        try:
            coins_off_str = data['priceModule']['promotionSellingPointTags'][0]['elementList'][1]['textContent']
            coins_off_value = float(coins_off_str[0:coins_off_str.find('%')])/100
            coins_off = coins_off_value*price_float_value
        except Exception as e:
            pass
        price_float_value -= coins_off
        price = round(price_float_value, 2)
    
    except Exception as e:
        #print(f'Erro no scraping do produto: {url}, de sku: {sku_id}')
        print(e)
        price = -2
    return price, retalier

if __name__ == '__main__':
    print(scrape('https://pt.aliexpress.com/item/1005005195329185.html?pdp_ext_f=%7B%22ship_from%22:%22CN%22,%22sku_id%22:%2212000032093838411%22%7D&&scm=1007.25281.317569.0&scm_id=1007.25281.317569.0&scm-url=1007.25281.317569.0&pvid=202bf4cf-e566-480d-8387-5057587255f5&utparam=%257B%2522process_id%2522%253A%252240%2522%252C%2522x_object_type%2522%253A%2522product%2522%252C%2522pvid%2522%253A%2522202bf4cf-e566-480d-8387-5057587255f5%2522%252C%2522belongs%2522%253A%255B%257B%2522floor_id%2522%253A%252236569244%2522%252C%2522id%2522%253A%252232032614%2522%252C%2522type%2522%253A%2522dataset%2522%257D%252C%257B%2522id_list%2522%253A%255B%255D%252C%2522type%2522%253A%2522gbrain%2522%257D%255D%252C%2522pageSize%2522%253A%252220%2522%252C%2522language%2522%253A%2522pt%2522%252C%2522scm%2522%253A%25221007.25281.317569.0%2522%252C%2522countryId%2522%253A%2522BR%2522%252C%2522scene%2522%253A%2522TopSelection-Waterfall%2522%252C%2522tpp_buckets%2522%253A%252221669%25230%2523265320%252341_21669%25234190%252319164%2523645_15281%25230%2523317569%25230%2522%252C%2522x_object_id%2522%253A%25221005005195329185%2522%257D&pdp_npi=2%40dis%21BRL%21R%24%20341%2C53%21R%24%20167%2C35%21%21%21%21%21%400b89a67f16777212742615583e0942%2112000032093838411%21gdf&spm=a2g0o.tm1000000741.4408202170.0&aecmd=true', '12000032093838411'))