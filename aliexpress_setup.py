from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
service = Service(ChromeDriverManager().install())

url = 'https://s.click.aliexpress.com/e/_DkMBEZx'

def setup_ali():
    browser = webdriver.Chrome(service=service, options=chrome_options)
    browser.get(url)
    time.sleep(3)
    browser.get_cookies()
    while True:
        try:
            browser.find_element(By.XPATH, '//*[@id="header-zip-input"]').send_keys('38402-680')
            break
        except:
            browser.find_element(By.XPATH, '//*[@id="nav-global"]/div[4]').click()
    time.sleep(3)
    browser.find_element(By.XPATH, '//*[@id="header-zip-option"]/li/div').click()
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="nav-global"]/div[4]/div/div/div/div[5]/button').click()
    time.sleep(5)
    browser.get_cookies()
    print(browser.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div/div[2]/div[4]/div/span').text)
    print('AliExpress setup finished!')