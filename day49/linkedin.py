from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import os
import time

login_screen = "https://www.linkedin.com/login"

search_results = "https://www.linkedin.com/jobs/search/?currentJobId=3507874964&distance=25&f_AL=true&f_E=1&f_WT=2&geoId=103644278&keywords=cyber%20security&location=United%20States&refresh=true"

# save the path to the Chrome Driver as a variable
service = Service("/Applications/chromedriver")
# create a driver for Chrome
driver = webdriver.Chrome(service=service)

# open up a webpage
driver.get("https://www.linkedin.com/login")
driver.maximize_window()

# find and save the username and password fields
user_name = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
signin_button = driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div[1]/form/div[3]/button")


# click into the username field and enter username
user_name.click()
user_name.send_keys(os.environ.get("USERNAME"))

# click into the password field and enter password
password.click()
password.send_keys(os.environ.get("PASSWORD"))

# click the signin button
signin_button.click()

time.sleep(5)

driver.get(search_results)

time.sleep(2)
# click on first job on the page
jobs = driver.find_elements(By.CSS_SELECTOR, "jobs-search-results__list-item")

# For each job in the jobs list, click the Save button, scroll down to the bottom of the right hand pane and then
# click the Follow button.
for job in jobs:
    job.click()
    time.sleep(4)
    save_button = driver.find_element(By.CLASS_NAME, "jobs-save-button")
    save_button.click()
    time.sleep(2)
    # Click the right hand rail and scroll down to the bottom of the page to reveal the Follow button.
    job_detail = driver.find_element(By.CLASS_NAME, "jobs-search__right-rail")
    job_detail.click()
    html = driver.find_element(By.CLASS_NAME, "html")
    html.send_keys(Keys.END)
    time.sleep(2)
    # Exception handling for instances in which the company does not have a Follow button.
    try:
        follow = driver.find_element(By.TAG_NAME, "follow")
        follow.click()
        time.sleep(2)
    except:
        continue

while True:
    pass



