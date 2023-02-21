from chrome_options import service, chrome_options
from selenium import webdriver
from selenium.webdriver.common.by import By

def coupon_validation(description, product):
    return True

def get_response(url):
    price = -2
    store = None
    navegador = webdriver.Chrome(service=service, options=chrome_options)
    navegador.get(url)
    print(navegador)
    try:
        price = float(navegador.find_element(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span/span[2]/span[2]').text.replace('.', '') + '.' + navegador.find_element(By.XPATH, '//*[@id="corePrice_feature_div"]/div/span/span[2]/span[3]').text)
        store = navegador.find_element(By.XPATH, '//*[@id="sellerProfileTriggerId"]').text
    except Exception as e:
        try:
            store = navegador.find_element(By.XPATH, '//*[@id="tabular-buybox"]/div[1]/div[4]/div/span').text
        except:
            try:
                navegador.find_element(By.XPATH, '//*[@id="outOfStock"]/div/div[1]/span').text
                price = -1
            except Exception as e:
                pass
    return price, store

def scrape(url, params=None):
    webdriver.Chrome(service=service, options=chrome_options)
    return get_response(url)
    #concurrent.futures.ThreadPoolExecutor().map(get_response, urls)
    
if __name__ == '__main__':
    scrape(['https://amzn.to/3Sz6WnT'])
