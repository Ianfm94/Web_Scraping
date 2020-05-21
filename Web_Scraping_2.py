import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import chromedriver_binary

pd.options.display.float_format = '{:.0f}'.format

is_link = 'https://finance.yahoo.com/quote/AAPL/history?p=AAPL'
driver = webdriver.Chrome("webdriver.exe")
driver.get(is_link)
html = driver.execute_script('return document.body.innerHTML;')
soup = BeautifulSoup(html,'lxml')

close_price_2 = [entry.text for entry in soup.find_all('span', {'data-reactid=61'})]
print(close_price_2)

