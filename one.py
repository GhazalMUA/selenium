from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
import time


# chrome_options = Options()
# # chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
# chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # To avoid detection
# chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")  # Fake user-agent




driver= webdriver.Chrome()
url = 'https://www.mastersportal.com/'
wait = WebDriverWait(driver, 10)

driver.get(url) 
what_to_search = driver.find_element(by=By.ID,value='HomeWhat')  
what_to_search.send_keys('Computer')   
what_to_search.send_keys(Keys.ENTER)
which_country = driver.find_element(by=By.ID , value='HomeWhere')
which_country.send_keys('Germany')
which_country.send_keys(Keys.ENTER)

time.sleep(10)

lst=[]
cols= ['title','price','duration','university','location']
title = driver.find_elements(by=By.CLASS_NAME , value='StudyName')
price = driver.find_elements(by=By.CLASS_NAME , value='TuitionValue')
duration = driver.find_elements(by=By.CLASS_NAME , value='DurationValue')
university = driver.find_elements(by=By.CLASS_NAME , value='OrganisationName')
location = driver.find_elements(by=By.CLASS_NAME , value='OrganisationLocation')

for (t, p, d, u, l) in zip(title,price,duration,university,location):
    print(f"Title: {t.text}, Price: {p.text}, Duration: {d.text}, University: {u.text}, Location: {l.text}")
    lst.append([t.text, p.text, d.text, u.text, l.text])
    
driver.quit()    

dataf = pd.DataFrame(lst,columns=cols)
dataf.to_csv('out.csv')

print("Data successfully saved to 'out.csv'")
