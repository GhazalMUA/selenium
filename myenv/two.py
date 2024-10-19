from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Open the website
url = 'https://www.mastersportal.com/'
driver.get(url)

# Wait for the search input to be present and interactable
wait = WebDriverWait(driver, 10)  # Timeout set to 10 seconds

try:
    # Wait for the 'What' search box to appear
    what_to_search = wait.until(EC.presence_of_element_located((By.ID, 'HomeWhat')))
    what_to_search.send_keys('Computer')
    what_to_search.send_keys(Keys.ENTER)

    # Wait for the 'Where' input to appear
    which_country = wait.until(EC.presence_of_element_located((By.ID, 'HomeWhere')))
    which_country.send_keys('Germany')
    which_country.send_keys(Keys.ENTER)
    
    # Continue with the rest of your code...
    # Wait for the page to load the results if necessary
    time.sleep(5)  # This is optional, but sometimes helps with slow page loads

except Exception as e:
    print(f"Error: {e}")

finally:
    # If debugging, you can leave the browser open
    driver.quit()
