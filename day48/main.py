from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# save the path to the Chrome Driver as a variable
service = Service("/Applications/chromedriver")
# create a driver for Chrome
driver = webdriver.Chrome(service=service)

# open up a webpage
driver.get("https://www.amazon.com/346E2CUAE-Frameless-UltraWide-Adjustable-Replacement/dp/B08KFSMGJ8/ref=sr_1_3?crid=QFJYW9STVI3B&keywords=ultrawide+monitor+usb-c&qid=1680136303&rnid=1248877011&s=electronics&sprefix=ultrawide+monitor+usb-c%2Celectronics%2C125&sr=1-3")
# get the element with the price
price = driver.find_element(By.CLASS_NAME, value='a-price-whole')
print(f'${price.text}.99')
# close the browser - using driver.quit() will close all tabs
driver.close()

