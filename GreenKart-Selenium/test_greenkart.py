import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

serv_obj = Service("D:\\Essential\\Browser Driver\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(10)

# url_validation
actual_url = "https://rahulshettyacademy.com/seleniumPractise/#/"
exp_url = driver.current_url
assert actual_url == exp_url

# title_validation
actual_title = "GreenKart - veg and fruits kart"
exp_title = driver.title
assert actual_title == exp_title

# search_box functionality
search_box = driver.find_element(By.XPATH, "//input[@type='search']")
assert search_box.is_enabled()
assert search_box.is_displayed()
search_box.send_keys("Brocolli")
product = driver.find_element(By.XPATH, "//div[@class='products']/div/h4")
assert "Brocolli" in product.text

search_box.clear()
search_box.send_keys("ber")
time.sleep(3)
products = driver.find_elements(By.XPATH, "//div[@class='products']/div/h4")
add_to_cart = driver.find_elements(By.XPATH, "//div[@class='products']/div/h4/parent::div/div/button")
for i in range(len(products)):
    # print(ele.text)
    if "ber" in products[i].text:
        assert add_to_cart[i].is_enabled() and add_to_cart[i].is_displayed()
        add_to_cart[i].click()


# cart_btn
cart_btn = driver.find_element(By.XPATH, "//div[@class='cart']/a/img")
assert cart_btn.is_displayed() and cart_btn.is_enabled()
cart_btn.click()


# checkout_btn
checkout_btn = driver.find_element(By.XPATH, "//button[normalize-space()='PROCEED TO CHECKOUT']")
assert checkout_btn.is_displayed() and checkout_btn.is_enabled()
checkout_btn.click()


# table
table_ele = driver.find_elements(By.XPATH, "//table[@id='productCartTables']/tbody/tr/td[5]")
total = 0
for ele in table_ele:
    total += float(ele.text)

actual_total = int(driver.find_element(By.XPATH, "//span[@class='totAmt']").text)
assert actual_total == total


place_order_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Place Order']")
assert place_order_btn.is_displayed() and place_order_btn.is_enabled()
place_order_btn.click()


country_drpdwn = Select(driver.find_element(By.XPATH, "//div[@class='wrapperTwo']/div/select"))
country_drpdwn.select_by_visible_text("Bangladesh")

driver.find_element(By.XPATH, "//input[@class='chkAgree']").click()
driver.find_element(By.XPATH, "//button[normalize-space()='Proceed']").click()

time.sleep(10)
