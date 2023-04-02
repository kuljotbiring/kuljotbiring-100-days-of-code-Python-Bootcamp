from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from time import sleep


def click_cookie(cookie_btn):
    """Find cookies and clicks repeatedly for 5 mins
    it contains a .05 sleep to allow multiple clicks"""
    # cookie = driver.find_element(By.XPATH, '//*[@id="bigCookie"]')
    sleep(.02)
    cookie_btn.click()


def get_score():
    """get the number of cookies earned by grabbing the element
    and performing string operations to get the total cookie count
    formats the web-element to just the number of cookies and removes any commas
    in the raw_cookies variable"""
    curr_score = driver.find_element(By.ID, "cookies")
    score_text = str(curr_score.text)
    cookie_score = score_text.split()
    raw_cookies = cookie_score[0]
    # remove commas so number can be processed as integer
    num_cookies = int(''.join(c for c in raw_cookies if c.isdigit()))

    return num_cookies


def buy_upgrades():
    """Attempt to buy the upgrade available if have enough cookies"""
    # loop through and save prices in a list
    for i in range(4, -1, -1):
        try:
            upgrade = driver.find_element(By.XPATH, f'//*[@id="upgrade{i}"]')
            upgrade.click()
        except:
            pass


def product_prices():
    """Get the current product prices"""
    # list to store prices
    price_list = []
    # loop through and save prices in a list
    for i in range(0, 19):
        try:
            item = driver.find_element(By.XPATH, f'//*[@id="productPrice{i}"]')
            item = str(item.text)
            item = (''.join(c for c in item if c.isdigit()))
            item = int(item)
            price_list.append(item)
        except ValueError:
            pass

    return price_list


def buy_products():
    """Attempts to buy most expensive items with the amount of cookies remaining"""
    cookies = get_score()
    prices = product_prices()
    i = len(prices) - 1
    while prices and (cookies >= prices[0]):
        if cookies >= prices[i]:
            try:
                item_to_buy = driver.find_element(By.XPATH, f'//*[@id="product{i}"]')
                item_to_buy.click()
            except:
                continue
        else:
            i -= 1
        cookies = get_score()
        prices = product_prices()


# save the path to the Chrome Driver as a variable
service = Service("/Applications/chromedriver")
# create a driver for Chrome
driver = webdriver.Chrome(service=service)

# open up a webpage
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.maximize_window()
english = driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
english.click()
sleep(5)
cookie = driver.find_element(By.XPATH, '//*[@id="bigCookie"]')
end_time = time.time() + 300

while time.time() < end_time:
    # save the 5 seconds to check what we can buy
    end_click_time = time.time() + 15
    while time.time() < end_click_time:
        click_cookie(cookie)
    buy_upgrades()
    buy_products()

cookie_per_s = driver.find_element(By.ID, "cookiesPerSecond").text
print(cookie_per_s)