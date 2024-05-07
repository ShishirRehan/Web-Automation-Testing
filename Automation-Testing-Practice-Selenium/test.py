import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

serv_obj = Service("D:\\Essential\\Browser Driver\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
act = ActionChains(driver)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)


# Name
class NameOperation:
    def nameperation(self):
        driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Shishir Rehan")


nameObj1 = NameOperation()
nameObj1.nameperation()
time.sleep(2)


# Email
class EmailOperation:
    def emailoperation(self):
        driver.find_element(By.XPATH, "//input[@id='email']").send_keys("shishir@email.com")


emailobj = EmailOperation()
emailobj.emailoperation()
time.sleep(2)


# Phone
class PhoneOperation:
    def phoneoperation(self):
        driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("0123456789")


phoneobj = PhoneOperation()
phoneobj.phoneoperation()
time.sleep(2)


# Address
class AddressOperation:
    def addressoperation(self):
        driver.find_element(By.XPATH, "//textarea[@id='textarea']").send_keys("Daulatpu, Kushtia, Khulna, Bangladesh")


addressobj = AddressOperation()
addressobj.addressoperation()
time.sleep(3)


# Gender
class GenderOperation:
    def genderoperation(self):
        elements = driver.find_elements(By.XPATH, "//input[@name='gender']")
        for element in elements:
            if element.get_attribute("value") == "male":
                element.click()


genderobj = GenderOperation()
genderobj.genderoperation()
time.sleep(2)


# Days
class DayOperation:
    def dayoperation(self):
        days = driver.find_elements(By.XPATH, "//input[contains(@id, 'day')]")
        for day in days:
            if day.get_attribute("value") == "friday":
                day.click()


dayObj = DayOperation()
dayObj.dayoperation()
time.sleep(3)


# Country
class CountryOp:
    def countryoperation(self):
        countrys = Select(driver.find_element(By.XPATH, "//select[@id='country']"))
        countrys.select_by_visible_text("India")


countryobj = CountryOp()
countryobj.countryoperation()
time.sleep(3)


# Colors
class ColorsOp:
    def colorsoperation(self):
        colors = Select(driver.find_element(By.XPATH, "//select[@id='colors']"))
        colors.select_by_visible_text("Green")


colorobj = ColorsOp()
colorobj.colorsoperation()
time.sleep(3)


# Web Table(Table Handling)
class WebTableOp:
    def webtableoperation(self):
        noofcolumns = driver.find_elements(By.XPATH, "//div[@class='widget-content']/table/tbody/tr/th")
        noofrows = driver.find_elements(By.XPATH, "//div[@class='widget-content']/table/tbody/tr")
        for row in range(2, len(noofrows)+1):
            for column in range(1, len(noofcolumns)+1):
                print(driver.find_element(By.XPATH, "//div[@class='widget-content']/table/tbody/tr["+str(row)+"]/td["+str(column)+"]").text, end="      ")
            print(" ")


webtableobj = WebTableOp()
webtableobj.webtableoperation()


# Pagination Table(Table handling)
class PaginationTable:
    def paginationtableop(self):
        noofcolumns = driver.find_elements(By.XPATH, "//div[@class='table-container']/table/thead/tr/th")
        noofrows = driver.find_elements(By.XPATH, "//div[@class='table-container']/table/tbody/tr")
        for row in range(1, len(noofrows)+1):
            for column in range(1, len(noofcolumns)):
                print(driver.find_element(By.XPATH, "//div[@class='table-container']/table/tbody/tr["+str(row)+"]/td["+str(column)+"]").text, end="    ")
            print()


paginationtableobj = PaginationTable()
paginationtableobj.paginationtableop()


# Tabs(Browser Window Handling)
class Tab:
    def taboperation(self):
        driver.find_element(By.XPATH, "//input[@class='wikipedia-search-input']").send_keys("Selenium")
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@class='wikipedia-search-button']").click()
        time.sleep(2)


tabobj = Tab()
tabobj.taboperation()
time.sleep(5)


# New Browser Window
class NewWindow:
    def newtabop(self):
        driver.find_element(By.XPATH, "//button[normalize-space()='New Browser Window']").click()
        tabs = driver.window_handles
        for ele_id in range(len(tabs)):
            if ele_id == 1:
                driver.switch_to.window(tabs[ele_id])
                title = driver.title
                print(title)
                time.sleep(3)
        driver.switch_to.window(tabs[0])


newtabobj = NewWindow()
newtabobj.newtabop()
time.sleep(5)


# JS Alerts
class Alert:
    def alertoperation(self):
        driver.find_element(By.XPATH, "//button[normalize-space()='Alert']").click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[normalize-space()='Confirm Box']").click()
        time.sleep(2)
        confirm_box = driver.switch_to.alert
        confirm_box.dismiss()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[normalize-space()='Prompt']").click()
        time.sleep(2)
        prompt = driver.switch_to.alert
        prompt.send_keys("Shishir Rehan")
        prompt.accept()


alertobj = Alert()
alertobj.alertoperation()
time.sleep(3)


# Double Click
class DoubleClickOp:
    def doubleclick(self):
        act.double_click(driver.find_element(By.XPATH, "//button[normalize-space()='Copy Text']")).perform()


doubleclickobj = DoubleClickOp()
doubleclickobj.doubleclick()
time.sleep(3)


# Drag & Drop
class DragDrop:
    def dragdropoperation(self):
        act.drag_and_drop(driver.find_element(By.XPATH, "//div[@id='draggable']"), driver.find_element(By.XPATH, "//div[@id='droppable']")).perform()


dragdropobj = DragDrop()
dragdropobj.dragdropoperation()
time.sleep(2)


# Slider
class Slide:
    def slideoperation(self):
        act.drag_and_drop_by_offset(driver.find_element(By.XPATH, "//div[@id='slider']/span"), 80, 0).perform()


slideobj = Slide()
slideobj.slideoperation()
time.sleep(5)


# Frames
class Frame:
    def frameoperation(self):
        driver.switch_to.frame("frame-one796456169")
        driver.find_element(By.XPATH, "//input[@id='RESULT_TextField-0']").send_keys("Shishir")
        time.sleep(2)
        gender = driver.find_elements(By.XPATH, "//div[@id='q2']/table/tbody/tr/td/label")
        for ele in gender:
            if ele.text == "Male":
                ele.click()
        time.sleep(2)
        # driver.find_element(By.XPATH, "//input[@id='RESULT_TextField-2']").send_keys("08/05/1998")
        driver.find_element(By.XPATH, "//div[@id='q4']/span").click()
        year = Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-year']"))
        year.select_by_visible_text("1998")
        dates = driver.find_elements(By.XPATH, "//div[@id='ui-datepicker-div']/table/tbody/tr/td/a")
        month = driver.find_element(By.XPATH, "//div[@class='ui-datepicker-title']/span").text
        for date in dates:
            if date.text == "5":
                date.click()
        time.sleep(2)
        job = Select(driver.find_element(By.XPATH, "//select[@id='RESULT_RadioButton-3']"))
        job.select_by_visible_text("QA Engineer")
        driver.switch_to.default_content()


frameobj = Frame()
frameobj.frameoperation()
time.sleep(3)


# Resizable
class Resize:
    def resizeoperation(self):
        act.drag_and_drop_by_offset(driver.find_element(By.XPATH, "//div[@id='resizable']/div[3]"), 500, 0).perform()


resizeobj = Resize()
resizeobj.resizeoperation()
time.sleep(5)


