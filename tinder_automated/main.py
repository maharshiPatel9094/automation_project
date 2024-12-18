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
my_number = os.getenv("MY_NUMBER")

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

time.sleep(3)
handle_cookies()
time.sleep(3)

# make the create account button click
button_click = driver.find_element(By.XPATH,value='//*[@id="main-content"]/div/div[2]/button/div[2]/div[2]/div')
button_click.click()

# click the facebook login page 
time.sleep(3)
fb_login = driver.find_element(By.XPATH,value='//*[@id="q-920667245"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div[2]/div/div')
fb_login.click()

#handle the second window  
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title) #should print the title Facebook

#Login and hit enter
email = driver.find_element(By.XPATH, value='//*[@id="email"]')
password = driver.find_element(By.XPATH, value='//*[@id="pass"]')
email.send_keys(my_number)
password.send_keys(my_password)
password.send_keys(Keys.ENTER)

#switch back to the base window
driver.switch_to.window(base_window)
print(driver.title)
