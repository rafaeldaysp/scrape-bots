from bs4 import BeautifulSoup
import json
import re
from response_handler import get_response

def scrape(url, sku_id):
    price = -1
    retalier = None
    desconto = None
    slogan_banner_off = 0
    try:
        r = get_response(url)
        match = re.search(r'data: ({.+})', r.text).group(1)
        data = json.loads(match)
        retalier = data['storeModule']['storeName']
        price_info = data['skuModule']['skuPriceList']
        qtd_produtos = len(price_info)
        try:
            slogan_banner = data['middleBannerModule']['uniformMiddleBanner']['sloganBanner']
            if slogan_banner == 'Preço exclusivo na primeira compra':
                slogan_banner_off = 15.98
                print(slogan_banner_off)
            ## colocar aqui quando tiver desconto de 15 a cada 150 
        except:
            pass
        for i in range(0, qtd_produtos):
            if str(price_info[i]['skuId']) == sku_id:
                price = price_info[i]['skuVal']['skuActivityAmount']['formatedAmount']
                if price_info[i]['skuVal']['availQuantity'] == 0:
                    return -1, retalier
        price_float_value = float(price[3:].replace('.', '').replace(',', '.')) + slogan_banner_off
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
        
        coins_off = 0
        try:
            coins_off_str = data['priceModule']['promotionSellingPointTags'][0]['elementList'][1]['textContent']
            coins_off_value = float(coins_off_str[0:coins_off_str.find('%')])/100
            coins_off = coins_off_value*price_float_value
        except Exception as e:
            pass
    
        shop_coupon_off = 0
        for i in range(len(coupons)):
            try:
                if price_float_value > coupons_conditions[i]:
                    shop_coupon_off = coupons[i]
            except Exception as e:
                pass
        desconto = shop_coupon_off + coins_off
        price_float_value = price_float_value - desconto
        price = round(price_float_value, 2)
        desconto = str(round(desconto, 2)).replace('.', ',')
    
    except Exception as e:
        print(f'Erro no scraping do produto: {url}, de sku: {sku_id}')
        print(e)
      
    return price, retalier

if __name__ == '__main__':
    pass