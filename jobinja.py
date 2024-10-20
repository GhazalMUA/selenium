
'''
    this is a data scraping from jobinja.ir website 
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
url = 'https://jobinja.ir/'
driver.get(url)

# jobinja intorie ke vaghti yebafr enter mikoni mire search mikone
search_title = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div/form/div[1]/input')

search_title.click()
search_title.send_keys('frontend')
search_title.send_keys(Keys.ENTER)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'c-jobListView__titleLink')))


col = ['title', 'company', 'logo', 'location']

titles = driver.find_elements(by=By.CLASS_NAME, value='c-jobListView__titleLink')
companies = driver.find_elements(by=By.XPATH, value='//ul[contains(@class, "c-jobListView__meta")]//li[1]//span')
logos = driver.find_elements(by=By.CLASS_NAME, value='o-listView__itemIndicatorImage')
location = driver.find_elements(by=By.XPATH , value='//ul[contains(@class, "c-jobListView__meta")]//li[2]//span')

if len(titles) == len(companies) == len(logos)  == len(location):
    list=[]
    for (t, com, l , loc) in zip(titles, companies, logos, location):
        print(f' title: {t.text }, company: {com.text }, logo: {l.get_attribute("src") }, location: {loc.text}')
        list.append([t.text if t else "N/A", com.text if com else "N/A", l.get_attribute('src') if l else "N/A", loc.text if loc else "N/A"])

    data = pd.DataFrame(list, columns= col)
    print(data)
    data.to_csv('jobs1.csv')    
    print('that was successfull.')

else:
    print('Error: The number of titles, companies, logos, type_of_job and location does not match.')
    print(f"Number of titles found: {len(titles)}")
    print(f"Number of companies found: {len(companies)}")
    print(f"Number of logos found: {len(logos)}")
    print(f"Number of location found: {len(location)}")

time.sleep(5)        
driver.quit()    



