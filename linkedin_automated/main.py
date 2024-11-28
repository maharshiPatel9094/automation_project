from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import time

# load env variables
load_dotenv()

# get env variables
ACCOUNT_EMAIL = os.getenv("MY_EMAIL")
ACCOUNT_PASSWORD = os.getenv("MY_PASSWORD")

# url
# URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
URL = "https://www.linkedin.com"

# keep the window open
chrome_options = webdriver.ChromeOptions() #chrome options
chrome_options.add_experimental_option("detach",True) #options


# object
driver = webdriver.Chrome(options = chrome_options)
driver.maximize_window() #max the window size
driver.get(URL) #get the url page

# click the sign in button
time.sleep(2) #sleep window to load the page properly
sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in_button.click()

# fill up the sign in form 
enter_username = driver.find_element(By.ID,value= "username")
enter_username.send_keys(ACCOUNT_EMAIL)

enter_password = driver.find_element(By.ID,value= "password")
enter_password.send_keys(ACCOUNT_PASSWORD)

# click sign in to sign-in
time.sleep(4)

click_sign_in = driver.find_element(By.XPATH,value= '//*[@id="organic-div"]/form/div[4]/button')
click_sign_in.click()



# quit
# driver.quit()