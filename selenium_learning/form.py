from selenium import webdriver #get the webdriver 
from selenium.webdriver.common.by import By #get the By method


URL = "https://secure-retreat-92358.herokuapp.com/"

# chrome options to keep the window on 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)


driver = webdriver.Chrome(options = chrome_options) #drive chrome browser and webdrivr object
driver.maximize_window() #maximize window to prevent interpretations
driver.get(URL) #get the website url

# selecting the form imput fields
fname_placeholder = driver.find_element(By.NAME,value="fName")
lname_placeholder = driver.find_element(By.NAME,value="lName")
email_placeholder = driver.find_element(By.NAME,value="email")


fname_placeholder.send_keys("test123") #sending the keys to first name
lname_placeholder.send_keys("test") #sending the keys to last name 
email_placeholder.send_keys("test@gmail.com") #sending the email keys to email 

submit = driver.find_element(By.CSS_SELECTOR, value= "form button")
submit.click()

driver.quit() #close all tabs