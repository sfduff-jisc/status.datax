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
services = []
things = []
things = p_element.find_elements(By.CSS_SELECTOR,"h2[class*='text-xl font-medium'")

for thing in things:
    print(thing.text)
    services.append( thing.text )
print()

print('Statuses')
statuses = []
states = []
states = p_element.find_elements(By.CSS_SELECTOR,"p[class*='text-base'")

for state in states:
    print(state.text)
    statuses.append( state.text )

print()

print('times')
times = []
others = []
others = p_element.find_elements(By.CSS_SELECTOR,"p[class*='text-sm'")

for other in others:
    print(other.text)
    times.append( other.text )


print()
print( services )
print( statuses )
print( times )

status_page = {}


for service in services:
    status_page.update(service)

    '''
    
    append(status_pa 
    for status in statuses:
        for tim3 in times:
            status_pa = {}
            status_pa['service']=service
            status_pa['status']=status
            status_pa['time']=tim3
            status_page.( status_pa )

print()
print( status_page )

'''