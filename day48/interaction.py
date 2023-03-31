from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys


# save the path to the Chrome Driver as a variable
service = Service("/Applications/chromedriver")
# create a driver for Chrome
driver = webdriver.Chrome(service=service)

# open up a webpage
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# get the number of articles on Wikipedia
articles = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/main/div[3]/div[3]/div[1]/div[1]/div/div[3]/a[1]")

print(articles.text)
# get a link by name and have Selenium click on the link
create_account = driver.find_element(By.LINK_TEXT, "Log in")
create_account.click()
# now at log in screen select into the username field
user_name = driver.find_element(By.NAME, "wpName")
# input what to type in the field
user_name.send_keys("Python")
# select into the password field
password = driver.find_element(By.NAME, "wpPassword")
# input what to type in the field
password.send_keys("abc123")
# get a hold of the remember me button
remember = driver.find_element(By.NAME, "wpRemember")
# click the remember me button
remember.click()
# get a hold of the login button
login = driver.find_element(By.NAME, "wploginattempt")
# click the login button
login.click()

# using input to keep window open
input("Press Enter to Continue")
# close the window
driver.close()
