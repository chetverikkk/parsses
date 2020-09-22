import sys
from selenium import webdriver
import time
from bs4 import BeautifulSoup
link = ""
browser = webdriver.Chrome()
browser.get(link)
time.sleep(10)
while True:
    for i in range:
        coef = browser.find_elements_by_css_selector('a.graph-label > span')
        time.sleep(10)
        coef2 = browser.find_elements_by_css_selector('a.graph-label > span')
        if coef[i] != coef2[i]:
            print(coef[i].text)