from requests_html import HTMLSession
import time
import app
HTMLSession(browser_args=["--no-sandbox"])
time.sleep(15)
app.main()