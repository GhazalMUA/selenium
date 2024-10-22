from my_pass import LOGIN_USERNAME , LOGIN_PASSWORD
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

'''
    global variables
'''
SEARCH_ITEM = 'amiroism'




'''
    this will block popups
'''
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2  # 1 for Allow, 2 for Block
})


driver = webdriver.Chrome(options=chrome_options)
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

#notif to save password after login successfully. you can click on not now
try:
    pass_notif = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mount_0_0_B3"]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div/div/div/div[3]/div/div[2]/div[2]/div')))
    pass_notif.click()
except:
    print('saving pass notif didnt appear. continue...')

time.sleep(2)
    
#looking for search button and search smth     
try:      
    search_field = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//input[@aria-label="Search Facebook"]')))
    print('search field was found')  
    search_field.send_keys(SEARCH_ITEM)
    print('typing was successfull')
    time.sleep(3)
    search_field.send_keys(Keys.ENTER)                                                                    
except Exception as e:
    print('i couldnt find search field, {e}')

#here you should wait in search part till the crawler find `see all` button.
try:
    see_all = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//a[@aria-label="See all"]')))
    print('found see all') 
    see_all.click()  
    print('i clicked on see all')  
except Exception as e:
    print(f'i couldnt find see all button , {e}')
time.sleep(2)    

#finding target accout/search word in the suggested list
try:
    targeted_search = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Amir Hatami (Amiro)')]")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", targeted_search)
    time.sleep(2)
    targeted_search.click()
except Exception as e:
    print(f'your requested profile not found. {e}')


time.sleep(5)    
driver.quit()


