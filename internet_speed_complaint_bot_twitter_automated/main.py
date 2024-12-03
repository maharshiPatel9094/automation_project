import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


TWITTER_URL = "https://twitter.com/login"
INTERNET_TEST_URL = "https://www.speedtest.net/"

# load env
load_dotenv()

# get env 
my_email = os.getenv("MY_EMAIL")
my_password = os.getenv("MY_PASSWORD")
promised_up = os.getenv("PROMISED_UP")
promised_down = os.getenv("PROMISED_DOWN")

# class for internet
class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions() #chrome options
        self.chrome_options.add_experimental_option("detach",True) #chrome option to keep the window open
        self.driver = webdriver.Chrome(options= self.chrome_options) #driver object
        self.driver.maximize_window() #max window
        self.up = 0 #initially set to 0
        self.down = 0 #initially set to 0
        
    def get_internet_speed(self):
        '''This function get the internet speed.'''
        self.driver.get(INTERNET_TEST_URL)
        
        # clcik the go button to check the speed
        sleep(3)
        self.go_button = self.driver.find_element(By.XPATH,value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        self.go_button.click()
        
        sleep(60)
        self.handle_cookie = self.driver.find_element(By.XPATH,value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/a')
        self.handle_cookie.click()
        self.down = self.driver.find_element(By.XPATH,value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH,value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        
        print(self.up)
        print(self.down)
    
    def tweet_at_provider(self):
        '''This function tweet at provider.'''
        self.driver.get(TWITTER_URL)
        
        # 
        sleep(5)
        self.cross_button = self.driver.find_element(By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div[1]/button')
        self.cross_button.click()

        sleep(3)
        self.cookie_cross_button = self.driver.find_element(By.XPATH,value='//*[@id="layers"]/div/div[1]/div/div/div/button')
        self.cookie_cross_button.click()

        sleep(3)
        self.sign_in_button = self.driver.find_element(By.LINK_TEXT,value="Sign in")
        self.sign_in_button.click()
        
        sleep(3)
        self.email_text = self.driver.find_element(By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        self.email_text.send_keys(my_email)
        
        sleep(3)
        self.next_button = self.driver.find_element(By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div')
        self.next_button.click() 
        
        sleep(3)
        self.password_text = self.driver.find_element(By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        self.password_text.send_keys(my_password)
        
        sleep(3)
        self.login_button = self.driver.find_element(By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button/div')
        self.login_button.click()
        
        sleep(3)
        self.draft_post_button = self.driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div')
        self.draft_post_button.click()
        
        sleep(3)
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {promised_down}down/{promised_up}up?"
        self.tweet_message = self.driver.find_element(By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        self.tweet_message.send_keys(tweet)
        
        sleep(3)
        self.send_post_button = self.driver.find_element(By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/button/div/span/span')
        self.send_post_button.click()
        
# initialize the object 
internet_bot  = InternetSpeedTwitterBot()
internet_bot.get_internet_speed()
internet_bot.tweet_at_provider()


# quit window
# driver.quit()