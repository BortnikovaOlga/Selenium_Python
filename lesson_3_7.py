# Явные ожидания. Проверка видимости, кликабельности, наличие текста у элемента
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver,25)

driver.get("http://demo.automationtesting.in/JqueryProgressBar.html")
# явное ожидание(EC) для проверки что кнопка "Close" невидима
wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR,'div.ui-dialog-buttonset button')))
# нажать кнопку "Start Download"
download_btn = driver.find_element_by_css_selector('button[id="downloadButton"]')
download_btn.click()
# явное ожидание(EC) для проверки, что кнопка "Cancel Download" кликабельна
cancel_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'div.ui-dialog-buttonset button')))
# проверка, что кнопка называется "Cancel Download"
assert cancel_btn.text == 'Cancel Download'
# нажать кнопку отмены загрузки
cancel_btn.click()
# снова нажать на загрузку
download_btn.click()
# явное ожидание(EC) для проверки что в окне присутствует текст "Complete!" после успешной загрузки
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'div.progress-label'),'Complete!'))
driver.quit()



