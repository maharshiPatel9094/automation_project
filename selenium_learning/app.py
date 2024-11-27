from selenium import webdriver #get webdriver from selenium 
from selenium.webdriver.common.by import By #get the By 

URL = "https://en.wikipedia.org/wiki/Main_Page" #wikipedia page url

# keep the chrome on 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)


driver = webdriver.Chrome(options= chrome_options) #drive the chrome browser & webdriver object
driver.get(URL) #get the url data 


# slecting the desired elements
articlecount = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(articlecount.text) #get the number of total articles from the wikipedia page


driver.quit() #make sure we exit all the tabs