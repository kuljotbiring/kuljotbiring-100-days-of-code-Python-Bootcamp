from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from time import sleep


def play_game():
    """ Function waits for page to load. Find cookies and clicks repeatedly for 5 mins
    it contains a .05 sleep to allow multiple clicks"""
    sleep(5)
    cookie = driver.find_element(By.XPATH, '//*[@id="bigCookie"]')
    end_time = time.time() + 10
    while time.time() < end_time:
        sleep(.02)
        cookie.click()


def get_score():
    """get the number of cookies earned by grabbing the element
    and performing string operations to get the total cookie count"""
    curr_score = driver.find_element(By.ID, "cookies")
    score_text = str(curr_score.text)
    cookie_score = score_text.split()
    num_cookies = cookie_score[0]
    return num_cookies

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


