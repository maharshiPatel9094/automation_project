import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


URL = "https://twitter.com/login"

# load env
load_dotenv()

# get env 
my_email = os.getenv("MY_EMAIL")
my_password = os.getenv("MY_PASSWORD")
promised_up = os.getenv("PROMISED_UP")
promised_down = os.getenv("PROMISED_DOWN")

# class for internet
class InternetSpeedTwitterBot:
    def __init__(self,up,down):
        self.chrome_options = webdriver.ChromeOptions() #chrome options
        self.chrome_options.add_experimental_option("detach",True) #chrome option to keep the window open
        self.driver = webdriver.Chrome(options= self.chrome_options) #driver object
        self.driver.maximize_window() #max window
        self.driver.get(URL) #get url
        self.up = 0 #initially set to 0
        self.down = 0 #initially set to 0
        
    def get_internet_speed():
        '''This function get the internet speed.'''
        pass
    
    def tweet_at_provider():
        '''This function tweet at provider.'''
        pass


# initialize the object 
internet_bot  = InternetSpeedTwitterBot()
internet_bot.get_internet_speed()
internet_bot.tweet_at_provider()


# quit window
# driver.quit()