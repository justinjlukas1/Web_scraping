
#https://medium.freecodecamp.org/better-web-scraping-in-python-with-selenium-beautiful-soup-and-pandas-d6390592e251

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import xlsxwriter

#launch url
url = "https://www.target.com/p/nintendo-switch-with-neon-blue-and-neon-red-joy-con/-/A-52189185"

#make dictionaries?
element_titles = ['item name', 
                  'store name', 
                  'item price', 
                  'store zip code', 
                  'order by date', 
                  'arrival date', 
                  'shipping cost', 
                  'store inventory']

element_xpaths = ['//*[@id="mainContainer"]/div/div/div[1]/div[1]/div[1]/h1/span',
                  '//*[@id="storeId-utilityNavBtn"]/div[2]',
                  '//*[@id="mainContainer"]/div/div/div[1]/div[2]/div/div[1]/span',
                  '//*[@id="mainContainer"]/div/div/div[1]/div[2]/div/div[6]/div/div[1]/div[1]/div/div[1]/a',
                  '//*[@id="mainContainer"]/div/div/div[1]/div[2]/div/div[6]/div/div[1]/div[2]/p',
                  '//*[@id="mainContainer"]/div/div/div[1]/div[2]/div/div[6]/div/div[1]/div[2]/div/div/span',
                  '//*[@id="mainContainer"]/div/div/div[1]/div[2]/div/div[6]/div/div[2]/div/div[1]/div[1]/div[1]/div[1]',
                  '//*[@id="mainContainer"]/div/div/div[1]/div[2]/div/div[6]/div/div[2]/div/div[1]/div[1]/div[1]/div[2]'
        ]

element_list = []

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('product_data.xlsx')
worksheet = workbook.add_worksheet()

row = 0
col = 0


# create a new Safari session
driver = webdriver.Safari()
driver.implicitly_wait(30)
driver.get(url)


for i in range(0, len(element_titles)):
    try:
        temp_element = driver.find_element(By.XPATH, element_xpaths[i])
        element_list.append(temp_element.get_attribute('innerText'))
    except Exception:
        try:
            temp_element = driver.find_element(By.XPATH, element_xpaths[i])
            element_list.append(temp_element.get_attribute('text'))
        except Exception:
            element_list.append(element_titles[i] + " not available")
               
driver.quit()

for title in element_titles:
    worksheet.write(row, col, title)
    col += 1

col = 0
row += 1
for element in element_list:
    worksheet.write(row, col, element)
    col += 1
    
workbook.close()