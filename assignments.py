from bots import acer_scrape, aliexpress_scrape, amazon_scrape, avell_scrape, carrefour_scrape, casasbahia_scrape, kabum_scrape, magalu_scrape, nave_scrape

MAIN_URL = 'https://bench-server-production.up.railway.app'
API_KEY = 'UfLk014eu5loeUzkBWi67ku9s2FGdNuFTmxcysQGO7BZS0NfIQQyCXpQ1GzAHDUHfQKTJDnAIBSQAOmYbnnczuoe5ys8maufkBpk73kbqGzeWYD9qGysLXidBMzWeDnN'
RETAILERS_FUNC = {'f0b30a9b-2ef4-40b9-85f9-7440a4680c0f': {'name': 'Amazon', 'scrape_func': amazon_scrape.scrape, 'coupon_validation_func': amazon_scrape.coupon_validation},
                  '813e0632-ff58-46fe-8bbd-5a0446df85d8': {'name': 'Kabum', 'scrape_func': kabum_scrape.scrape, 'coupon_validation_func': kabum_scrape.coupon_validation},
                  '760fc2a9-aaca-426f-8dcc-c7c2a4377d8b': {'name': 'AliExpress', 'scrape_func': aliexpress_scrape.scrape, 'coupon_validation_func': aliexpress_scrape.coupon_validation},
                  '': {'name': 'Acer', 'scrape_func': acer_scrape.scrape, 'coupon_validation_func': acer_scrape.coupon_validation}}