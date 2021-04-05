# Работа с вкладками. Переключение по вкладкам, явное ожидание для url, количества вкладок
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver,20)

driver.get("http://demo.automationtesting.in/Windows.html")
# переключиться в раздел "Open New Tabbed Windows"
driver.find_element_by_css_selector("div[id='Tabbed'] a button").click()
# переключиться во вторую вкладку
driver.switch_to.window(driver.window_handles[1])
assert driver.current_url == "https://www.selenium.dev/"
driver.close()
# переключиться в первую вкладку
driver.switch_to.window(driver.window_handles[0])
# переключиться в раздел "Separate Multiple Windows"
driver.find_element_by_css_selector('a[href="#Multiple"]').click()
driver.find_element_by_css_selector('div[id="Multiple"] button').click()
#  переключиться во второе окно
driver.switch_to.window(driver.window_handles[2])
# проверка url, используя явное ожидание
wait.until(EC.url_to_be("http://demo.automationtesting.in/Index.html"))
# Проверка, что в браузере открыто 3 вкладки, используя явное ожидание
print("открыто три вкладки ", wait.until(EC.number_of_windows_to_be(3)))
# заполнить поле эл.почты и нажать на ">"
driver.find_element_by_css_selector('input[id="email"]').send_keys("1@1.ru")
driver.find_element_by_css_selector('div[id="main"] a').click()
# проверка, что ссылка = "http://demo.automationtesting.in/Register.html"
wait.until(EC.url_to_be("http://demo.automationtesting.in/Register.html"))
driver.quit()