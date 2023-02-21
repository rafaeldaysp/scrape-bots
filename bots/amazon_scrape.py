from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
service = Service(ChromeDriverManager().install())

def coupon_validation(description, product):
    return True

def get_response(url):
    price = -2
    store = None
    navegador = webdriver.Chrome(service=service, options=chrome_options)
    navegador.get(url)
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
