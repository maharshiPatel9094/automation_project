import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
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
        
        # follower list
        sleep(3)
        # choose the path that makes scrolling bar green
        modal_xpath = ""
        modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)
        for _ in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as an HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)
        
    
    def follow():
        pass
    
    
    
insta_bot = InstaFollower()
insta_bot.login()
insta_bot.find_followers()
insta_bot.follow()