#¡/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Automate launching of Safari, leting the page load and reading the generated JS page to the jspage object 
jspage = webdriver.Safari()
jspage.get('https://status.datax.jisc.ac.uk')
time.sleep(2)

# Gather item title in a list
titles = jspage.find_elements(By.CSS_SELECTOR,"h2[class*='text-xl font-medium'")
item_titles = []
for title in titles:
    item_titles.append( title.text )

# Gather item states in a list
states = jspage.find_elements(By.CSS_SELECTOR,"p[class*='text-base'")
item_states = []
for state in states:
    item_states.append( state.text )

# Gather item update times in a list
details = jspage.find_elements(By.CSS_SELECTOR,"p[class*='text-sm'")
item_details = []
for other in details:
    item_details.append( other.text )

# Construct page data records from titles, statuses and times
page_data = {}
c = 0
for title in item_titles:
    page_data.update( {title : { 'status': item_states[c], 'updated': item_details[c]}})
    c=c+1

# Output scraped data
print()
for record in page_data:
    print( record )
    print( page_data[record] )
    
  