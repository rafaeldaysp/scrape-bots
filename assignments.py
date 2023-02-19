from bots import acer_scrape, aliexpress_scrape, amazon_scrape, avell_scrape, carrefour_scrape, casasbahia_scrape, kabum_scrape, magalu_scrape, nave_scrape

RETAILERS_FUNC = {'57ad8275-bd9a-4ea7-9a5d-e5ff76760900': {'name': 'Amazon', 'scrape_func': amazon_scrape.scrape, 'coupon_validation_func': amazon_scrape.coupon_validation},
                  'c56ada6a-a3e7-4b2f-a8d6-17e358472b81': {'name': 'Kabum', 'scrape_func': kabum_scrape.scrape, 'coupon_validation_func': kabum_scrape.coupon_validation},
                  'c301b951-1dc7-47e6-b51f-d6da74b4f1cf': {'name': 'AliExpress', 'scrape_func': aliexpress_scrape.scrape, 'coupon_validation_func': aliexpress_scrape.coupon_validation}}