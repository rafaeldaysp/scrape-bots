from bs4 import BeautifulSoup
from requests_html import HTMLSession

def scrape(url):
    session = HTMLSession(browser_args=["--no-sandbox", "--user-agent='Testing'"])
    r = session.get(url)
    r.html.render(sleep = 5)
    try:
        price = float(BeautifulSoup(r.html.raw_html, 'html.parser').find_all('h3', class_='MuiTypography-root MuiTypography-h3')[0].text.replace('.', '').replace(',', '.'))
    except Exception as e:
        print('Erro no produto da Avell', e)
    return price, 'Avell'

if __name__ == '__main__':
    scrape('https://avell.idevaffiliate.com/idevaffiliate.php?id=218&url=852')









'MuiTypography-root MuiTypography-h3'
