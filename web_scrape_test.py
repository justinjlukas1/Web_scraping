
#https://medium.freecodecamp.org/better-web-scraping-in-python-with-selenium-beautiful-soup-and-pandas-d6390592e251

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


#launch url
url = "https://www.target.com/p/nintendo-switch-with-neon-blue-and-neon-red-joy-con/-/A-52189185"

# create a new Safari session
driver = webdriver.Safari()
driver.implicitly_wait(30)
driver.get(url)

try:
    store_name_element = driver.find_element(By.XPATH, '//*[@id="storeId-utilityNavBtn"]/div[2]')
    print(store_name_element.get_attribute('innerText'))
except Exception:
    print "There's no store name available"
   
try:
    item_name_element = driver.find_element(By.XPATH, '//*[@id="mainContainer"]/div/div/div[1]/div[1]/div[1]/h1/span')
    print(item_name_element.get_attribute('innerText'))
except Exception:
    print "There's no item name available"
       
try:
    price_element = driver.find_element(By.XPATH, '//*[@id="mainContainer"]/div/div/div[1]/div[2]/div/div[1]/span')
    print(price_element.get_attribute('innerText'))
except Exception:
    print "There's no pricce available"
    
try:
    zip_code_element = driver.find_element(By.XPATH, '//*[@id="mainContainer"]/div/div/div[1]/div[2]/div/div[6]/div/div[1]/div[1]/div/div[1]/a')
    print(zip_code_element.get_attribute('innerText'))
except Exception:
    print "There's no zip code available"
    
try:
    order_by_element = driver.find_element(By.XPATH, '//*[@id="mainContainer"]/div/div/div[1]/div[2]/div/div[6]/div/div[1]/div[2]/p')
    print(order_by_element.get_attribute('innerText'))
except Exception:
    print "There's no order by time available"
    
try:
    arrival_date_element = driver.find_element(By.XPATH, '//*[@id="mainContainer"]/div/div/div[1]/div[2]/div/div[6]/div/div[1]/div[2]/div/div/span')
    print(arrival_date_element.get_attribute('innerText'))
except Exception:
    print "There's no arrival date available"
    
try:
    shipping_cost_element = driver.find_element(By.XPATH, '//*[@id="mainContainer"]/div/div/div[1]/div[2]/div/div[6]/div/div[2]/div/div[1]/div[1]/div[1]/div[1]')
    print(shipping_cost_element.get_attribute('innerText'))
except Exception:
    print "There's no shipping cost available"
   
try:
    current_inventory_element = driver.find_element(By.XPATH, '//*[@id="mainContainer"]/div/div/div[1]/div[2]/div/div[6]/div/div[2]/div/div[1]/div[1]/div[1]/div[2]')
    print(current_inventory_element.get_attribute('innerText'))
except Exception:
    print "There's no current inventory available"
    
driver.quit()
