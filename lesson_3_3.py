# Модальные окна: alert, confirm, prompt
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
# driver.get("http://demo.automationtesting.in/WebTable.html")
# driver.find_element_by_xpath('//a[@href="SwitchTo.html"][1]').click()
# driver.find_element_by_xpath('//a[@href="Alerts.html"]').click()
# переход из меню блокируется фреймом с рекламой
driver.get("http://demo.automationtesting.in/Alerts.html")

# нажать на кнопку "click the button to display an alert box:"
driver.find_element_by_css_selector('button[onclick="alertbox()"]').click()
alert = driver.switch_to.alert
# assert alert.text == "I am an alert box!" # как вариант
if alert.text != "I am an alert box!":
    print('ошибка, ожидался текст в окне "I am an alert box!"')
alert.accept()
# получить текущий url
alerts_url = driver.current_url
time.sleep(4)

# открыть новую вкладку
driver.execute_script("window.open();")
driver.switch_to.window(driver.window_handles[1])
driver.get(alerts_url)

driver.find_element_by_css_selector('a[href="#CancelTab"]').click()
time.sleep(3)
# нажать на кнопку "click the button to display a confirm box"
driver.find_element_by_css_selector('button[onclick="confirmbox()"]').click()
confirm = driver.switch_to.alert
confirm.dismiss()
alerts_url = driver.current_url
time.sleep(3)

# открыть новую вкладку
driver.execute_script("window.open();")
driver.switch_to.window(driver.window_handles[2])
driver.get(alerts_url)

driver.find_element_by_css_selector('a[href="#Textbox"]').click()
time.sleep(3)
# нажать на кнопку "click the button to demonstrate the prompt box"
driver.find_element_by_css_selector('button[onclick="promptbox()"]').click()
prompt = driver.switch_to.alert
prompt.send_keys("Ура! Задание выполнено!")
prompt.accept()
time.sleep(3)
driver.quit()

