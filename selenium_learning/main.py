from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.python.org/"

# Keep the browser window open after execution
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create the driver object with the specified options
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# scrapping python org to get the list of upcoming events and dates 
event_times = driver.find_elements(By.CSS_SELECTOR,value= ".event-widget time") #gives list of selenium tags.
event_names = driver.find_elements(By.CSS_SELECTOR, value= ".event-widget li a")#if getting unnecessary output be more specific as here we used li bcz we were getting one unnecessary output.

events = {}
for n in range(len(event_times)):
    # n+1 makes the dictionary numbering start from 1
    events[n+1] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }

print(events)
# for time in event_times:
#     print(time.text)#text property does not works on list so we have to loop through it.

# for name in event_names:
    # print(name.text)#name of the events 


driver.quit()  # Comment this out if you want the browser to stay open