# upload, script
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Register.html")
# заполнить элементы формы
driver.find_element_by_css_selector("input[ng-model='FirstName']").send_keys("TestFirst")
driver.find_element_by_css_selector("input[ng-model='LastName']").send_keys("TestLast")
driver.find_element_by_css_selector("input[ng-model='EmailAdress']").send_keys("1@test.ru")
driver.find_element_by_css_selector("input[ng-model='Phone']").send_keys("1234567899")
driver.find_element_by_css_selector("input[value='Male']").click()
Select(driver.find_element_by_id('countries')).select_by_visible_text("Russia")
Select(driver.find_element_by_id('yearbox')).select_by_value("1999")
Select(driver.find_element_by_css_selector("select[ng-model='monthbox']")).select_by_value("May")
Select(driver.find_element_by_css_selector("select[ng-model='daybox']")).select_by_value("1")
driver.find_element_by_id("firstpassword").send_keys("Qq1234")
driver.find_element_by_id("secondpassword").send_keys("Qq1234")
driver.find_element_by_id("imagesrc").send_keys("C:\\temp\\logotip.png")
driver.execute_script("window.scrollBy(0, 300);")
driver.find_element_by_id("submitbtn").click()
time.sleep(6)

next_url = 'http://demo.automationtesting.in/WebTable.html'
print(("Ошибка, ожидалась страница ","Переход на страницу ")[driver.current_url == next_url] + next_url )
driver.quit()

