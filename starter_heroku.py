from requests_html import HTMLSession
import time
import app
def start():
    HTMLSession(browser_args=["--no-sandbox"])
    time.sleep(15)
    app.main()
if __name__ == '__main__':
    start()