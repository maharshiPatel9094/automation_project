from selenium import webdriver #get webdriver from selenium 
from selenium.webdriver.common.by import By #get the By 
from selenium.webdriver.common.keys import Keys

URL = "https://en.wikipedia.org/wiki/Main_Page" #wikipedia page url

# keep the chrome on 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)


driver = webdriver.Chrome(options= chrome_options) #drive the chrome browser & webdriver object
driver.maximize_window() #maximise the window to prevent unnecessary pop ups hiding the page 
driver.get(URL) #get the url data 


# slecting the desired elements
articlecount = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(articlecount.text) #get the number of total articles from the wikipedia page


# articlecount.click() #clicking to elemnts using selenium driver 


# using link text to find the element 
# just write the same name as in the browser to select the particular link element
# link text is specifically designed for selecting the linked elements 
all_portals = driver.find_element(By.LINK_TEXT, value= "Community portal")
# all_portals.click()

search = driver.find_element(By.NAME,value= "search")
search.send_keys("Python",Keys.ENTER) #write the input



# driver.quit() #make sure we exit all the tabs