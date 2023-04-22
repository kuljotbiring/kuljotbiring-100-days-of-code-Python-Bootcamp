from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#-----------Driver Setting(no auto close the window)------------**
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
chrome_driver_path = Service("/Applications/chromedriver")
driver = webdriver.Chrome(options=options, service=chrome_driver_path)

driver.maximize_window() # For maximizing window
driver.implicitly_wait(20) # gives an implicit wait for 20 seconds

driver.get("https://orteil.dashnet.org/cookieclicker/")

#-----------Search for the element & interactive------------**
language = driver.find_element(By.CLASS_NAME, "langSelectButton")
language.click()
driver.implicitly_wait(10)

one_min = time.time() + 60 * 1  # 1 minutes
timeout = time.time() + 60 * 20  # 20 minutes

time.sleep(5)

while True:
    #----- aim to prevent error <stale element reference: element is not attached to the page document> ----**
    cookie_button_0 = driver.find_element(By.ID, "bigCookie")
    cookie_button_0.click()
    cookie_button_1 = driver.find_element(By.ID, "bigCookie")
    cookie_button_1.click()

    if time.time() > one_min:
        #----- check money bank -------**
        money_bank = driver.find_element(By.ID, 'cookies')
        money_in_hand = money_bank.text.split(' ')[0].replace(",", "")

        #------list all item & price--------**
        prices = driver.find_elements(By.CSS_SELECTOR, 'span.price')
        item_price = [n.text.replace(",", "") for n in prices]
        print(f"price: {item_price}")

        products = driver.find_elements(By.CSS_SELECTOR, 'div.title productName')
        all_item = []
        for x in range(19):
            ppp = driver.find_element(by='id', value=f"productName{x}")
            all_item.append(ppp.text)
        print(f"all items: {all_item}")

        show_item_position = [all_item.index(n) for n in all_item if n != '']
        showed_item_nbr = len(show_item_position)
        print(f"showed item nbr: {showed_item_nbr}")

        #----- check if can buy latest product -------**
        if int(money_in_hand) > int(item_price[showed_item_nbr - 1]):
            print(f"Have: {money_in_hand} cookies")
            item_to_buy = driver.find_element(By.ID, f"product{showed_item_nbr - 1}")
            print(f"Can buy: {item_to_buy.text} \n")
            for n in range(10):
                item_to_buy.click()
        else:
            print("Not enough money\n")

        one_min = time.time() + 60 * 1

    #------ check cps number --------**
    if time.time() > timeout:
        driver.implicitly_wait(30)
        cps_tag = driver.find_element(By.XPATH, '//*[@id="cookies"]')
        cps = cps_tag.text.split('\n')[1]
        print(f"cookie {cps}")
        break