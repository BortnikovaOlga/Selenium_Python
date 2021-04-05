# Практическое задание: элементы
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()

driver.find_element_by_id("menu_pim_viewPimModule").click()
time.sleep(3)
# переход в карточку первого случайного пользователя
driver.find_element_by_xpath("//table//tr[1]//td[2]/a").click()
# радиокнопки gender
personal_optGender1 = driver.find_element_by_id("personal_optGender_1")
personal_optGender2 = driver.find_element_by_id("personal_optGender_2")
gender_male = True
# проверка, что радиокнопка с противоположным полом сотрудника в данный момент недоступна для выбора
if personal_optGender1.get_attribute("checked"):
    assert personal_optGender2.get_attribute("disabled")
elif personal_optGender2.get_attribute("checked"):
    assert personal_optGender1.get_attribute("disabled")
    gender_male = False
else:
    print("не выбран пол")

# проверка, что селектор Nationality в данный момент недоступен для выбора
personal_cmbNation = driver.find_element_by_id("personal_cmbNation")
assert personal_cmbNation.get_attribute("disabled")

# нажать кнопку "Edit"
btn_save_edit = driver.find_element_by_css_selector('input[id="btnSave"]')
btn_save_edit.click()

# Изменить пол сотрудника на противоположный
# проверка, что радиокнопка с полом сотрудника действительно выбрана
if gender_male:
    personal_optGender2.click()
    assert personal_optGender2.get_attribute("checked")
    time.sleep(3)
    # вернуть первоначальный пол сотрудника
    personal_optGender1.click()
else:
    personal_optGender1.click()
    assert personal_optGender1.get_attribute("checked")
    time.sleep(3)
    # вернуть первоначальный пол сотрудника
    personal_optGender2.click()

# В селекторе Nationality выберать самую последнюю страну в списке
option = driver.find_element_by_css_selector('#personal_cmbNation option:last-child')
Select(personal_cmbNation).select_by_value(option.get_attribute("value"))
# проверка, что в селекторе Nationality выбрана последняя страна в списке
assert option.get_attribute("checked")
time.sleep(3)
# в селекторе Nationality выберать вариант "-- Select --"
Select(personal_cmbNation).select_by_visible_text("-- Select --")
time.sleep(3)
btn_save_edit.click()
driver.quit()


