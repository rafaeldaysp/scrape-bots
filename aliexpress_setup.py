import requests
import re
import json

url = 'https://www.aliexpress.us/item/1005005184541227.html?spm=a2g0o.detail.1000014.9.29ac5900YSCKl0&gps-id=pcDetailBottomMoreOtherSeller&scm=1007.40050.281175.0&scm_id=1007.40050.281175.0&scm-url=1007.40050.281175.0&pvid=34092b7c-a370-468a-b5bb-220313819447&_t=gps-id%3ApcDetailBottomMoreOtherSeller%2Cscm-url%3A1007.40050.281175.0%2Cpvid%3A34092b7c-a370-468a-b5bb-220313819447%2Ctpp_buckets%3A668%232846%238110%231995&pdp_ext_f=%7B%22sku_id%22%3A%2212000032018499830%22%2C%22sceneId%22%3A%2230050%22%7D&pdp_npi=3%40dis%21USD%2166.24%2152.99%21%21%21%21%21%40211b444516770380559527707ec95f%2112000032018499830%21rec%21US%21&gatewayAdapt=4itemAdapt'

headers = {'Accept-Language': 'pt-BR,pt;q=0.9',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
           #'cookie': 'xman_t=bihJm9DwnQHIornbBqSbcLRsZh3pYzjOhtsuLt6XNA44ySDY8pVjSt0ieRAQToTZ; _ga=GA1.1.116850409.1670721971; _ga_save=yes; xman_f=Eh95/sIl1+t/Y2WkZFdvWh+OPWFKF0HmFPaZpObI4PgbPGaZRY7uTBsMJjqMZ+a3icmBUOEkUnzbnvG5Ob+dTTMZuxX1IkJ9VonlMOqvyC3bfsOI1YLeHg==; XSRF-TOKEN=f804aac9-0008-40c4-9bc5-526afda1888a; intl_locale=en_US; acs_usuc_t=x_csrf=318d1zjrt0vv&acs_rt=3f3462ac61714e7fb68e8d963d66f2b8; AKA_A2=A; _m_h5_tk=0b335f4a3fc0ba00cd7035972b1f60db_1677040422666; _m_h5_tk_enc=9aac1893ee8a657cb6390930d9d281d0; xman_us_f=x_locale=en_US&x_l=0&x_c_chg=0&acs_rt=4ba0548134764b7786731ef60a8d595b; aep_history=keywords%5E%0Akeywords%09%0A%0Aproduct_selloffer%5E%0Aproduct_selloffer%091005005184541227; l=fBLMDdNrTdYkfczzBO5C-urza779fBdXGsPzaNbMiIEGa6s1UF_FGOCePuuy0dtjQT50qUKrl5ZFzdn9Slz_WxGNb6vNckOosZve8e__E-ZF.; tfstk=cTmdB-qw-CAn4iRubkLGz_ikEX-dawR819Nl2myndBlyi67O5svqmm3urew7MhvO.; isg=BL29V4TAgin4hSZFfiL4AR4izBm3WvGst_YYJX8FCpRDttHoTqlWfockYPLwNglk; aep_usuc_f=site=usa&c_tp=BRL&region=BR&b_locale=en_US&province=903200130000000000&city=903200130063000000; JSESSIONID=756567A2F479994594ABECE3B3096BF6; intl_common_forever=nlHWO7ppMgxSerS6Ra8KGww8PqD3KiM09nhcyjxp74eQvUf0EWNGGQ==',
           }

r = requests.get(url, headers=headers)
match = re.search(r'data: ({.+})', r.text).group(1)
data = json.loads(match)
retalier = data['storeModule']['storeName']
price_info = data['skuModule']['skuPriceList']
print(price_info)