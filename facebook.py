from my_pass import LOGIN_USERNAME , LOGIN_PASSWORD
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
url = 'https://facebook.com'
driver.get(url)
print('reached facebook')
time.sleep(5)

#accept cookies
try:
    popup = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="facebook"]/body/div[3]/div[2]/div/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div')))
    popup.click()
except:
    print('no cookie alart appear. continue...')
    
time.sleep(2)
print("Continuing with the rest of the script")

#find and fill username.
try:
    user_name_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,'email')))
    user_name_field.click()
    print('i found user key')
    user_name_field.send_keys(LOGIN_USERNAME)
    time.sleep(2)
    print('i typed username')
except Exception as e:
    print(f'unfortunatlly i didnt find and fill nusename field. this is the error: \n {e}')    

#find and fill password field    
try:    
    pass_field = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'pass')))
    pass_field.click()
    print('i found pass key')
    pass_field.send_keys(LOGIN_PASSWORD)
    pass_field.send_keys(Keys.ENTER)
    print('i typed pass key')
    time.sleep(2)
    print('logged in succesfully')
except Exception as e:
    print(f'unfortunatlly i didnt find and fill password field. this is the error: \n {e}')  

#a pop up for desktop notification. if appeared, click close button
try:
    desktop_notif = webdriver(driver,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id=":r3e:"]/div/div/div/div/div/div/div[2]/div')))
    desktop_notif.click()
except:
    print('notif after login didnt show')
    
time.sleep(20)    

try:      
    search_box = webdriver(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="mount_0_0_MY"]/div/div/div[1]/div/div[2]/div[3]/div/div/div[1]/div/div/label/input')))
    search_box.click()
    print('i found search field')
except Exception as e:
    print('i couldnt find search field')
driver.quit()