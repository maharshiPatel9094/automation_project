from selenium import webdriver
from selenium.webdriver.common.by import By
import time


URL = "http://orteil.dashnet.org/experiments/cookie/"

# keep the window on 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options= chrome_options)
driver.maximize_window()
driver.get(URL)


# get the cookie 
cookie = driver.find_element(By.ID,value="cookie")

# get items and ids
items = driver.find_elements(By.CSS_SELECTOR,value= "#store div")
item_ids = [item.get_dom_attribute("id") for item in items]
# print(item_ids)

# set time stamps
# time.time() gives the current time
timeout = time.time() + 5 #current time + 5sec
five_min_time = time.time() + 60*5 #5min from current time

all_prices = driver.find_elements(By.CSS_SELECTOR,value="#store b")


# item_prices= []
# for price in all_prices:
#     text_with_price = price.text #give full text e.g -> Cursor - 15
#     if text_with_price != "":
#         cost = int(text_with_price.split("-")[1].strip().replace(",",""))
#         item_prices.append(cost) 

# cookie_upgrades = {}
# for n in range(len(item_prices)):
#     cookie_upgrades[item_prices[n]] = item_ids[n]
    
# print(cookie_upgrades)
# {15: 'buyCursor', 100: 'buyGrandma', 500: 'buyFactory', 2000: 'buyMine', 7000: 'buyShipment', 50000: 'buyAlchemy lab', 1000000: 'buyPortal', 123456789: 'buyTime machine'}
# print(item_prices)
# # [15, 100, 500, 2000, 7000, 5000]

# game loop

while True:
    cookie.click() #click the cookie
    
    #every 5 sec check the upgrades available
    if time.time() > timeout:
        all_prices = driver.find_elements(By.CSS_SELECTOR,value="#store b")
        item_prices = [] #set empty list to get the items prices
        
        # get the int prices from this
        for price in all_prices:
            text_with_price = price.text #give full text e.g -> Cursor - 15
            if text_with_price != "":
                cost = int(text_with_price.split("-")[1].strip().replace(",",""))
                item_prices.append(cost) 
                
        # dict of store items and prices
        cookie_upgrades_dict = {}
        for n in range(len(item_prices)):
            cookie_upgrades_dict[item_prices[n]] = item_ids[n]


        # get the current cookie count
        cookie_count = driver.find_element(By.ID,value="money").text
        if "," in cookie_count:  #check if comma there or not in the count
            cookie_count = cookie_count.replace(",","")
        cookie_count = int(cookie_count) #store the int value
        
        
        
        # find the upgrades that we can currently purchase 
        affordable_upgrades = {}
        for cost,id in cookie_upgrades_dict.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id
                
        # purchase the most expensive item upgrade
        highest_affordable_price = max(affordable_upgrades)
        print(highest_affordable_price)
        to_purchase_id = affordable_upgrades[highest_affordable_price]
        
        
        driver.find_element(By.ID,value=to_purchase_id).click()
        
        timeout = time.time() + 5

    # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min_time:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break


# ['buyCursor', 'buyGrandma', 'buyFactory', 'buyMine', 'buyShipment', 'buyAlchemy lab', 'buyPortal', 'buyTime machine', 'buyElder Pledge']
# for item in items:
#     item_ids = item.get_attribute("id")
# print(item_ids)

# driver.quit()