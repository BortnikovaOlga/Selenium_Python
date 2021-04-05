# Неявное ожидание поиска элемента. Получение атрибута элемента
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("http://demo.automationtesting.in/DynamicData.html")
# Проверка текста заголовка
h3 = driver.find_element_by_css_selector('div.cont_box_center h3')
assert h3.text == 'Loading the data Dynamically'
# Нажать на кнопку "Get Dynamic Data"
driver.find_element_by_css_selector('button[id="save"]').click()
time.sleep(3)
# Вывод в консоль адреса ссылки, которая сгенерируется в теге img
img = driver.find_element_by_css_selector('div[id="loading"] img')
print("ссылка на изображение", img.get_attribute('src'))
driver.quit()