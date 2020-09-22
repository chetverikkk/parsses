from selenium import webdriver
import time
link = "https://csgorun.org"
browser = webdriver.Chrome()
browser.get(link)
time.sleep(5)
while True:
    coef = browser.find_elements_by_css_selector('a.graph-label:nth-child(1) > span:nth-child(1)')
    time.sleep(15)
    coef2 = browser.find_elements_by_css_selector('a.graph-label:nth-child(2) > span:nth-child(1)')
    if coef != coef2:
        f = open('C:\\zxc\\text.txt', 'a')
        f.write(str(coef[0].text) + ',' + ' ')
