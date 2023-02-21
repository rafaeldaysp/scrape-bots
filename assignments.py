from bots import acer_scrape, aliexpress_scrape, amazon_scrape, avell_scrape, b2w_scrape, \
    carrefour_scrape, casasbahia_scrape, kabum_scrape, magalu_scrape, nave_scrape

MAIN_URL = 'https://bench-server-production.up.railway.app'
API_KEY = 'UfLk014eu5loeUzkBWi67ku9s2FGdNuFTmxcysQGO7BZS0NfIQQyCXpQ1GzAHDUHfQKTJDnAIBSQAOmYbnnczuoe5ys8maufkBpk73kbqGzeWYD9qGysLXidBMzWeDnN'
RETAILERS_FUNC = {'f0b30a9b-2ef4-40b9-85f9-7440a4680c0f': {'name': 'Amazon', 'scrape_func': amazon_scrape.scrape, 'coupon_validation_func': amazon_scrape.coupon_validation},
                  '813e0632-ff58-46fe-8bbd-5a0446df85d8': {'name': 'Kabum', 'scrape_func': kabum_scrape.scrape, 'coupon_validation_func': kabum_scrape.coupon_validation},
                  '760fc2a9-aaca-426f-8dcc-c7c2a4377d8b': {'name': 'AliExpress', 'scrape_func': aliexpress_scrape.scrape, 'coupon_validation_func': aliexpress_scrape.coupon_validation},
                  '53b2e99e-a8e8-4d59-9305-5907b3b6f283': {'name': 'Acer', 'scrape_func': acer_scrape.scrape, 'coupon_validation_func': acer_scrape.coupon_validation},
                  'ba33ec55-a861-4750-b64a-02b2d2bbf585': {'name': 'Avell', 'scrape_func': avell_scrape.scrape, 'coupon_validation_func': avell_scrape.coupon_validation},
                  '4f47756e-0486-49ba-969c-4d6f01484f93': {'name': 'Carrefour', 'scrape_func': carrefour_scrape.scrape, 'coupon_validation_func': carrefour_scrape.coupon_validation},
                  'a60701d5-4ec5-45fe-b826-82e01c29b60b': {'name': 'Casas Bahia', 'scrape_func': casasbahia_scrape.scrape, 'coupon_validation_func': casasbahia_scrape.coupon_validation},
                  '327f768f-6ba6-4f97-a167-73b22d212db4': {'name': 'Magalu', 'scrape_func': magalu_scrape.scrape, 'coupon_validation_func': magalu_scrape.coupon_validation},
                  'b774c7e1-4162-4dc7-9e5a-9b215b5e58bb': {'name': 'Nave', 'scrape_func': nave_scrape.scrape, 'coupon_validation_func': nave_scrape.coupon_validation},
                  '14dfffca-fbe7-4342-866c-b5eb6b728c49': {'name': 'Submarino', 'scrape_func': b2w_scrape.scrape, 'coupon_validation_func': b2w_scrape.coupon_validation},
                  '56e7d0fb-425c-440d-87f3-cb11298977e1': {'name': 'Americanas', 'scrape_func': b2w_scrape.scrape, 'coupon_validation_func': b2w_scrape.coupon_validation},
                  '358bf3fc-d3b6-434c-b574-bc1a379ab7d8': {'name': 'Shoptime', 'scrape_func': b2w_scrape.scrape, 'coupon_validation_func': b2w_scrape.coupon_validation}}


