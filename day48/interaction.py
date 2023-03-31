from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# save the path to the Chrome Driver as a variable
service = Service("/Applications/chromedriver")
# create a driver for Chrome
driver = webdriver.Chrome(service=service)

# open up a webpage
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# get the number of articles on Wikipedia
articles = driver.find_elements(By.XPATH, "/html/body/div[1]/div/div[3]/main/div[3]/div[3]/div[1]/div[1]/div/div[3]/a[1]")


print(articles[0].text)

driver.close()
