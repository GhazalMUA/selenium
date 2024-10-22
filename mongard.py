'''
    mongard entekhab shode chonke ye meghdar bayad az balaye safe
    biam pain ke betonam icon ozviate vizhe ro bebinam.
    bad az click bar rooye ozviate vizhe bia tooye roadmap
    ye meghdar bia pain ta jadvalo bebini
    az jadval screenshot begir.
    
    
    up: in jaiye ke mikham ta jai biad scroll kone pain ke in element 
    daghighan balaye safe gharra begire.
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url='https://www.mongard.ir/'
driver = webdriver.Chrome()
driver.get(url)

try:
    driver.execute_script("window.scrollTo(0, 1000);")  # Scroll down by 500 pixels
    time.sleep(5)
    ozviat_vizhe = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR , '.products-section .custom-btn-blue, .action'))
        )

    driver.execute_script("arguments[0].scrollIntoView(true);", ozviat_vizhe)
    time.sleep(5)
    ozviat_vizhe.click()
    time.sleep(5)    
    print('successsfully find ozviatevizhe and click on it')
    time.sleep(2)
    roadmap = driver.find_element(by=By.XPATH, value='//div[contains(@class, "navbar-right-items")]//li[4]/a')
    roadmap.click()
    up = driver.find_element(by=By.XPATH, value='//*[@id="backend"]/h2[2]/span[2]/span/strong') 
    driver.execute_script("arguments[0].scrollIntoView(true);" , up)
    time.sleep(2)
    sc = driver.get_screenshot_as_file('mongardroadmapeSC.png') #take screenshot


except Exception as e:  
    print(f'Unsuccessful due to error: {e}')
finally:
    driver.quit()



