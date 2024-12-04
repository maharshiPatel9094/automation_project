import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys

# urls
LOGIN_URL = "https://www.instagram.com/accounts/login/"

# load env 
load_dotenv()

# get env var
my_email = os.getenv("MY_EMAIL")
my_password = os.getenv("MY_PASSWORD")
my_username = os.getenv("USERNAME")
SIMILAR_ACCOUNT = "chefsplate"

class InstaFollower:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach",True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.maximize_window()
        
    def login(self):
        self.driver.get(LOGIN_URL)
        
        sleep(5)
        self.username_text = self.driver.find_element(By.NAME,value="username")
        self.username_text.send_keys(my_email)
        self.password_text = self.driver.find_element(By.NAME,value="password")
        self.password_text.send_keys(my_password) 
        
        sleep(3)
        self.login_button = self.driver.find_element(By.XPATH,value='//*[@id="loginForm"]/div/div[3]/button/div')
        self.login_button.click()
    
        sleep(3)
        self.cookie_handle = self.driver.find_element(By.XPATH,value="//div[contains(text(), 'Not now')]")
        self.cookie_handle.click()
        
    def find_followers(self):
        sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")
        
        # followers button
        sleep(3)
        self.followers_button = self.driver.find_element(By.CSS_SELECTOR,value=f'ul li div a[href="/{SIMILAR_ACCOUNT}/followers/"]')
        self.followers_button.click()
        # choose the path that makes scrolling bar green 
    
    def follow(self):
        sleep(3)
        
        # Locate all "Follow" buttons using the XPath
        follow_buttons = self.driver.find_elements(By.XPATH, value='/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[3]/div/button')
        
        for button in follow_buttons:
            try:
                # Click the "Follow" button
                button.click()
                print("Clicked a follow button.")
                sleep(2)  # Small delay to mimic human interaction
                
                # Handle the cookie policy popup after each button click
                try:
                    cookie_policy_button = self.driver.find_element(By.XPATH, value='/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/button[2]')
                    cookie_policy_button.click()
                    print("Cookie policy button clicked.")
                    sleep(1)  # Short delay to ensure the next action can proceed smoothly
                except Exception as e:
                    print(f"Cookie policy popup not found after clicking button: {e}")
            except Exception as e:
                print(f"Error clicking a follow button: {e}")

            
    
    
    
insta_bot = InstaFollower()
insta_bot.login()
insta_bot.find_followers()
insta_bot.follow()