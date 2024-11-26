from bs4 import BeautifulSoup
import requests

url = "https://appbrewery.github.io/instant_pot/"


response = requests.get(url=url)#get the data
# print(response.content)


soup = BeautifulSoup(response.content,"html.parser")#soup object
# print(soup.prettify())

price_element = soup.find(class_ = "a-offscreen").getText()#contains -> <span class="a-offscreen">$99.99</span>
# print(price_element.split("$")[1])

price_value_without_currrency = price_element.split("$")[1]
# print(price_value_without_currrency)

float_price = float(price_value_without_currrency)