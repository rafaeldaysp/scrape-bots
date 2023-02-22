from bs4 import BeautifulSoup
from requests_html import HTMLSession
from fake_useragent import UserAgent

def coupon_validation(description, product):
    return True

def scrape(url, params = None):
    ua = str(UserAgent().chrome)
    try:
        session = HTMLSession(browser_args=["--no-sandbox", "--user-agent="+ua])
        r = session.get(url)
        r.html.render(sleep = 5)

    except:
        pass
    price = -1
    try:
        price = float(BeautifulSoup(r.html.raw_html, 'html.parser').find_all('h3', class_='MuiTypography-root MuiTypography-h3')[0].text.replace('.', '').replace(',', '.'))
    except Exception as e:
        print('Erro no produto da Avell', e)
    r.close()
    session.close()
    return price, 'Avell'

if __name__ == '__main__':
    pass