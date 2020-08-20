import selenium
import selenium.webdriver
from selenium.webdriver.chrome.options import Options
chrome_driver_path = ""
options = Options()
options.add_argument('--headless') #headless Webscraping
options.add_argument('--disable-gpu')

driver = selenium.webdriver.Chrome(chrome_driver_path, chrome_options=options)
