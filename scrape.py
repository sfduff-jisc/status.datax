#¡/usr/bin/env python3

import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time

driver = webdriver.Safari()
driver.get('https://status.datax.jisc.ac.uk')
time.sleep(2)

# https://www.zenrows.com/blog/scraping-javascript-rendered-web-pages#installing-the-requirements

p_element = driver.find_element(By.CSS_SELECTOR,"div[class*='flex flex-col flex-none items-center justify-center'")
print()
print(p_element.text)
print()

print('Services')
things = []
things = p_element.find_elements(By.CSS_SELECTOR,"h2[class*='text-xl font-medium'")

for thing in things:
    print(thing.text)
print()

print('Statuses')
states = []
states = p_element.find_elements(By.CSS_SELECTOR,"p[class*='text-base'")

for state in states:
    print(state.text)

print()

print('other')
others = []
others = p_element.find_elements(By.CSS_SELECTOR,"p[class*='text-sm'")

for other in others:
    print(other.text)


