import requests
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.common.by import By
from time import sleep  

URL = "https://appbrewery.github.io/Zillow-Clone/"
GOOGLE_FORM_URL = "https://forms.gle/zswNNqdoNBvZPw9Y8"
# print(response.request.headers) #get the request headers

# part-1 Scrape the links, addresses, and prices of the rental properties
headers = {
    'User-Agent': 'python-requests/2.32.3', 
    'Accept-Encoding': 'gzip, deflate, br', 
    'Accept': '*/*', 
    'Connection': 'keep-alive'
    }


response = requests.get(url=URL,headers=headers) #response
# print(response.text) #get website response
data = response.text
soup = BeautifulSoup(data,"html.parser")

# ---------------------------list of addresses---------------------
all_link_elements = soup.select(".StyledPropertyCardDataWrapper a")
all_link = [link["href"] for link in all_link_elements] 

# print(soup)
all_address_elements = soup.select(".StyledPropertyCardDataWrapper address") #get all the addresses by inspecting the website
all_addresses = [addresses.getText().strip().replace(" | "," ") for addresses in all_address_elements]
# print(all_addresses) #got all addresses in the proper list

# --------------------------list of prices-------------------------
all_prices_elements = soup.select(".PropertyCardWrapper span") #get all the addresses by select 
all_prices = [price.getText().replace("/mo","").split("+")[0] for price in all_prices_elements]
# print(all_prices) #get all the prices

# -----------------------------part2 -google form ----------------------------------
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

for n in range(len(all_link)):
    driver.get(GOOGLE_FORM_URL)
    sleep(3)
    
    address = driver.find_element(By.XPATH,value = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(By.XPATH,value= '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH,value= '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH,value= '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    
    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_link[n])
    submit_button.click()
