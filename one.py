from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 

import time

driver= webdriver.Chrome()
url = 'https://www.mastersportal.com/'

driver.get(url) 
what_to_search = driver.find_element(by=By.ID,value='HomeWhat')  
what_to_search.send_keys('Computer')   
what_to_search.send_keys(Keys.ENTER)
which_country = driver.find_element(by=By.ID , value='HomeWhere')
which_country.send_keys('Germany')
which_country.send_keys(Keys.ENTER)
time.sleep(15)
driver.quit()