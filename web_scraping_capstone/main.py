import requests
from bs4 import BeautifulSoup

URL = "https://appbrewery.github.io/Zillow-Clone/"
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
# print(soup)
all_address_elements = soup.select(".StyledPropertyCardDataWrapper address") #get all the addresses by inspecting the website
all_addresses = [addresses.getText().strip().replace(" | "," ") for addresses in all_address_elements]
# print(all_addresses) #got all addresses in the proper list

# --------------------------list of prices-------------------------
all_prices_elements = soup.select(".PropertyCardWrapper span") #get all the addresses by select 
all_prices = [price.getText().replace("/mo","").split("+")[0] for price in all_prices_elements]
# print(all_prices) #get all the prices