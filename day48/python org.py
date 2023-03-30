from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# save the path to the Chrome Driver as a variable
service = Service("/Applications/chromedriver")
# create a driver for Chrome
driver = webdriver.Chrome(service=service)

# open up a webpage
driver.get("https://www.python.org")
# make a dictionary for scraped values
time_place = {}

# use a loop to replace numbers in XPATH for time and location values
for i in range(1, 6):
    event_time = driver.find_element(By.XPATH, f'/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li[{i}]/time')
    event_location = driver.find_element(By.XPATH, f'/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li[{i}]/a')
    # insert values into dictionary
    time_place[event_time.text] = event_location.text

print(time_place)
