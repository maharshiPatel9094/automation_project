from bs4 import BeautifulSoup
import requests
import smtplib
import re
import os
from dotenv import load_dotenv

load_dotenv()#load env variables

url = "https://appbrewery.github.io/instant_pot/"
my_email = os.getenv("MY_EMAIL")
my_password = os.getenv("MY_PASSWORD")

# adding headers
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}

response = requests.get(url=url,headers=header)#get the data
# print(response.content)


soup = BeautifulSoup(response.content,"html.parser")#soup object
# print(soup.prettify())

price_element = soup.find(class_ = "a-offscreen").getText()#contains -> <span class="a-offscreen">$99.99</span>
# print(price_element.split("$")[1])

price_value_without_currrency = price_element.split("$")[1]
# print(price_value_without_currrency)

float_price = float(price_value_without_currrency)


# send email if:
# price below 100 dollars
# include title
# include current price
# include purchase link 

product_title = soup.find(id = "productTitle").getText()
cleaned_title = re.sub(r'\s+', ' ', product_title).strip()
# print(cleaned_title)


BUY_PRICE = 100

# condition to send the email
if float_price < BUY_PRICE:
    message = f"{product_title} is on sale for {price_element}"
    
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        result = connection.login(my_email,my_password)
        connection.sendmail(
            from_addr= my_email,
            to_addrs= my_email,
            msg= f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8") 
        )
        
