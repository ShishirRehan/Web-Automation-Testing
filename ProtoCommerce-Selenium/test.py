import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select


serv_obj = Service("D:\\Essential\\Browser Driver\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)


driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(10)


# 1st page
driver.find_element(By.XPATH, "//div[@class='container']/form/div[1]/input").send_keys("Shishir")
driver.find_element(By.XPATH, "//div[@class='container']/form/div[2]/input").send_keys("shishir@email.com")
driver.find_element(By.XPATH, "//div[@class='container']/form/div[3]/input").send_keys("123")
driver.find_element(By.XPATH, "//div[@class='container']/form/div[4]/input").click()
gender = Select(driver.find_element(By.XPATH, "//div[@class='container']/form/div[5]/select"))
gender.select_by_visible_text("Male")

driver.find_element(By.XPATH, "//input[@id='inlineRadio1']").click()
driver.find_element(By.XPATH, "//div[@class='container']/form/div[7]/input").send_keys("05-08-2002")
time.sleep(5)


# 2nd page
driver.find_element(By.XPATH, "//a[normalize-space()='Shop']").click()
products = driver.find_elements(By.XPATH, "//app-card-list[@class='row']/app-card/div/div[1]/h4")
buttons = driver.find_elements(By.XPATH, "//app-card-list[@class='row']/app-card/div/div[2]/button")

for i in range(len(products)):
    if products[i].text == "Nokia Edge":
        buttons[i].click()

driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
driver.find_element(By.XPATH, "//button[normalize-space()='Checkout']").click()
driver.find_element(By.XPATH, "//input[@id='country']").send_keys("bang")
driver.find_element(By.XPATH, "//div[@class='suggestions']/ul/li/a").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
successText = driver.find_element(By.CLASS_NAME, "alert-success").text

assert "Success! Thank you!" in successText

driver.get_screenshot_as_file("screen.png")

time.sleep(5)



