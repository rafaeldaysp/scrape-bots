from requests_html import HTMLSession
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def coupon_validation(description, product):
    return True

def scrape(url, params=None):
    price = -1
    store = None
    ua = str(UserAgent().chrome)
    try:
        session = HTMLSession(browser_args=["--no-sandbox", "--user-agent="+ua])
        r = session.get(url)
        r.html.render(sleep = 2)
    except Exception as e:
        session.close()
        r.close()
        print(e)
        return None, None
    site = BeautifulSoup(r.html.raw_html, 'html.parser')
    r.close()
    session.close()
    try:
        price = float(site.find('div', {'class': 'a-section a-spacing-none aok-align-center'}).find('span', class_='a-offscreen').text[2:].replace('.', '').replace(',', '.'))
        store = site.find_all('span', class_='a-size-small tabular-buybox-text-message')[1].text
    except:
        try:
            site.find('div', id='availability_feature_div').find('span', class_='a-size-medium a-color-price')
        except:
            price = -2
    return price, store


if __name__ == '__main__':
    print(scrape('https://www.amazon.com.br/dp/B0BJ6R9T2S?&linkCode=sl1&tag=lucasishii-20&linkId=bbf91b97e5323ba67d626d5304aeb404&language=pt_BR&ref_=as_li_ss_tl'))