from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import time

# URL
URL = "https://tinder.com/"

# load env
load_dotenv()

# get env var
my_email = os.getenv("MY_EMAIL")
my_password = os.getenv("MY_PASSWORD")

# chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

# driver object
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(URL) 

# Handle cookie consent popup
def handle_cookies():
    try:
        accept_button = driver.find_element(By.XPATH, '//*[@id="q807713831"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]/div')
        accept_button.click()
        print("Cookie consent accepted.")
    except Exception as error:
        print("No cookie consent popup found or already handled.", error)

# # login button click
# time.sleep(3)
# login_button = driver.find_element(By.LINK_TEXT, value="Log in")
# login_button.click()
# time.sleep(5)
# handle_cookies()
# time.sleep(6)
# fb_login = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
# fb_login.click()
# # driver.quit()

time.sleep(3)
handle_cookies()
time.sleep(3)
button_click = driver.find_element(By.XPATH,value='//*[@id="main-content"]/div/div[2]/button/div[2]/div[2]/div')
button_click.click()
time.sleep(3)
fb_login = driver.find_element(By.XPATH,value='//*[@id="q-920667245"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div[2]/div/div')
fb_login.click()