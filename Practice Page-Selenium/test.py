import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service("D:\\Essential\\Browser Driver\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
act = ActionChains(driver)


driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)


# Radio Button example
radio_buttons = driver.find_elements(By.XPATH, "//input[@name='radioButton']")
for ele in radio_buttons:
    if ele.get_attribute("value") == "radio2":
        ele.click()
        break

# OR
driver.find_element(By.CSS_SELECTOR, "[value='radio2']").click()
assert driver.find_element(By.CSS_SELECTOR, "[value='radio2']").is_selected()
time.sleep(3)


# Suggestion class example
driver.find_element(By.XPATH, "//input[@id='autocomplete']").send_keys("bang")
time.sleep(2)
act.key_down(Keys.ARROW_DOWN).perform()
act.key_up(Keys.ARROW_DOWN).perform()
act.key_down(Keys.RETURN).perform()
act.key_up(Keys.RETURN).perform()
time.sleep(5)

assert driver.find_element(By.XPATH, "//input[@id='autocomplete']").get_attribute("value") == "Bangladesh"


# Dropdown example
drp_down = Select(driver.find_element(By.XPATH, "//select[@id='dropdown-class-example']"))
drp_down.select_by_visible_text("Option2")

time.sleep(5)


# Checkbox Example
driver.find_element(By.XPATH, "//input[@id='checkBoxOption1']").click()
driver.find_element(By.XPATH, "//input[@id='checkBoxOption2']").click()
driver.find_element(By.XPATH, "//input[@id='checkBoxOption3']").click()

time.sleep(2)
assert driver.find_element(By.XPATH, "//input[@id='checkBoxOption1']").is_selected()
assert driver.find_element(By.XPATH, "//input[@id='checkBoxOption2']").is_selected()
assert driver.find_element(By.XPATH, "//input[@id='checkBoxOption3']").is_selected()
time.sleep(2)

driver.find_element(By.XPATH, "//input[@id='checkBoxOption1']").click()
driver.find_element(By.XPATH, "//input[@id='checkBoxOption2']").click()
driver.find_element(By.XPATH, "//input[@id='checkBoxOption3']").click()
time.sleep(2)


# # Switch Window example
# original_window = driver.current_window_handle
# assert len(driver.window_handles) == 1
# driver.find_element(By.XPATH, "//button[@id='openwindow']").click()
# windows = driver.window_handles
# for window in windows:
#     if window != original_window:
#         driver.switch_to.window(window)
#         assert driver.title == "QAClick Academy - A Testing Academy to Learn, Earn and Shine"
#         driver.close()
#         break
#
# time.sleep(3)


# Switch tab example
main_window = driver.current_window_handle
assert len(driver.window_handles) == 1
driver.find_element(By.XPATH, "//*[@id='opentab']").click()
time.sleep(2)
windows = driver.window_handles
for window in windows:
    if window != main_window:
        driver.switch_to.window(window)
        print(driver.title)
        assert driver.title == "QAClick Academy - A Testing Academy to Learn, Earn and Shine"
        driver.close()
        break
driver.switch_to.window(main_window)
print(driver.title)
time.sleep(3)


# Switch to Alert Example
driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Shishir")
assert driver.find_element(By.CSS_SELECTOR, "#name").get_attribute("value") == "Shishir"
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()
alert1 = driver.switch_to.alert
assert alert1.text == "Hello Shishir, share this practice page and share your knowledge"
alert1.accept()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Shishir")
driver.find_element(By.CSS_SELECTOR, "#confirmbtn").click()
alert2 = driver.switch_to.alert
assert alert2.text == "Hello Shishir, Are you sure you want to confirm?"
alert2.accept()
time.sleep(2)


# Element Displayed Example
assert driver.find_element(By.CSS_SELECTOR, "#displayed-text").is_displayed()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#hide-textbox").click()
assert not driver.find_element(By.CSS_SELECTOR, "#displayed-text").is_displayed()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#show-textbox").click()
assert driver.find_element(By.CSS_SELECTOR, "#displayed-text").is_displayed()
time.sleep(3)


# Web table example
rowno = len(driver.find_elements(By.CSS_SELECTOR, "[name='courses'] tbody tr "))
columnno = len(driver.find_elements(By.CSS_SELECTOR, "[name='courses'] tbody tr th"))


for r in range(2, rowno+1):
    for c in range(1, columnno+1):
        if driver.find_element(By.XPATH, "//table[@name='courses']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text == "Master Selenium Automation in simple Python Language":
            print(f"Course_Name: {driver.find_element(By.XPATH, "//table[@name='courses']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text}")
            print(f"Creator_Name: {driver.find_element(By.XPATH, "//table[@name='courses']/tbody/tr["+str(r)+"]/td["+str(c-1)+"]").text}")
            print(f"Course_Price: {driver.find_element(By.XPATH, "//table[@name='courses']/tbody/tr["+str(r)+"]/td["+str(c+1)+"]").text}")
            break

time.sleep(2)


# Web table fixed header
rownum = len(driver.find_elements(By.XPATH, "//div[@class='tableFixHead']/table/tbody/tr"))

total_amount = 0
for r in range(1, rownum+1):
    total_amount += int(driver.find_element(By.XPATH, "//div[@class='tableFixHead']/table/tbody/tr["+str(r)+"]/td[4]").text)

real_amount = driver.find_element(By.CSS_SELECTOR, ".totalAmount").text

assert str(total_amount) in real_amount


# MouseHover Example
act.move_to_element(driver.find_element(By.CSS_SELECTOR, "#mousehover")).click().perform()
time.sleep(3)
act.click(driver.find_element(By.XPATH, "//div[@class='mouse-hover-content']/a[1]")).perform()
time.sleep(3)
act.move_to_element(driver.find_element(By.CSS_SELECTOR, "#mousehover")).click().perform()
time.sleep(1)
act.click(driver.find_element(By.XPATH, "//div[@class='mouse-hover-content']/a[2]")).perform()


# Iframe example
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='courses-iframe']"))
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div/header/div[3]/div/div/div[2]/nav/div[2]/ul/li[6]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='username']").send_keys("Shishir")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='mobileno']").send_keys("0123456789")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("shishir@email.com")
time.sleep(2)
driver.find_element(By.XPATH, "//textarea[@id='requirements']").send_keys(
    "Hi. This is Shishir Rehan. Currently I'm learning SQA Engineering")
time.sleep(2)
select_program = Select(driver.find_element(By.XPATH, "//select[@id='programming-language']"))
select_program.select_by_visible_text("python")
time.sleep(2)
radio_btn = driver.find_elements(By.XPATH, "//input[@id='sharing']")
for ele in radio_btn:
    if ele.get_attribute("value") == "no":
        ele.click()
        break
time.sleep(2)
timezone = Select(driver.find_element(By.XPATH, "//select[@id='timezone']"))
timezone.select_by_visible_text("(GMT+06:00) Astana, Dhaka")
time.sleep(2)
radio_2 = driver.find_elements(By.XPATH, "//input[@id='afford']")
for element in radio_2:
    if element.get_attribute("value") == "no":
        element.click()
        break
time.sleep(2)
