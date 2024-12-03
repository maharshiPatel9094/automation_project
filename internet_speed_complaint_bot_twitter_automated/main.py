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
    
    def tweet_at_provider():
        '''This function tweet at provider.'''
        pass


# initialize the object 
internet_bot  = InternetSpeedTwitterBot()
internet_bot.get_internet_speed()
internet_bot.tweet_at_provider()


# quit window
# driver.quit()