from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from time import sleep


def play_game():
    sleep(7)
    cookie = driver.find_element(By.XPATH, '//*[@id="bigCookie"]')
    end_time = time.time() + 300
    while time.time() < end_time:
        sleep(.1)
        cookie.click()


# save the path to the Chrome Driver as a variable
service = Service("/Applications/chromedriver")
# create a driver for Chrome
driver = webdriver.Chrome(service=service)

# open up a webpage
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.maximize_window()
english = driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
english.click()

while True:
    play_game()
