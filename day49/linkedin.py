from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

login_screen = "https://www.linkedin.com/login"

search_results = "https://www.linkedin.com/jobs/search/?currentJobId=3564651424&distance=25&f_E=1&f_WT=2&geoId=103644278&keywords=cyber%20security&location=United%20States&refresh=true"

# save the path to the Chrome Driver as a variable
service = Service("/Applications/chromedriver")
# create a driver for Chrome
driver = webdriver.Chrome(service=service)

# open up a webpage
driver.get("https://www.linkedin.com/login")
driver.maximize_window()
