from requests_html import HTMLSession
from fake_useragent import UserAgent

def run():
    ua = UserAgent().chrome
    session = HTMLSession(browser_args=["--no-sandbox", "--user-agent="+ua])
    session.get('https://google.com/').html.render()
if __name__=='__name__':
    run()