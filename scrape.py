#¡/usr/bin/env python3

import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

driver = webdriver.Safari()
#PhantomJS()
driver.get('https://status.datax.jisc.ac.uk')

# https://www.zenrows.com/blog/scraping-javascript-rendered-web-pages#installing-the-requirements

p_element = driver.find_element(By.CSS_SELECTOR,"div[class*='flex flex-col flex-none items-center justify-center'")
print(p_element.text)



""""
page = requests.get('https://status.datax.jisc.ac.uk', headers=headers)

print('hello')

print( page.text)

soup = BeautifulSoup(page.text, 'html.parser')

quotes = []
quote_elements = soup.find_all('div', class_='grid grid-cols-2 gap-4 w-3/4')



for quote_element in quote_elements:
    # extracting the text of the quote
    text = quote_element.find('class', class_='w-full flex flex-row p-4 bg-green').text
    print( text)
    # extracting the author of the quote
    author = quote_element.find('p', class_='text-base').text
    print( author )
    print( text, author)


#
    # extracting the tag <a> HTML elements related to the quote
 #   tag_elements = quote_element.find('div', class_='tags').find_all('a', class_='tag')

    # storing the list of tag strings in a list
  #  tags = []
  #  for tag_element in tag_elements:
  #      tags.append(tag_element.text)
  #      //
  """