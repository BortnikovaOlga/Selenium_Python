from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver,20)
# driver.get("http://demo.automationtesting.in/WebTable.html")
# driver.find_element_by_css_selector('ul.navbar-nav>li:nth-child(9) a').click()
# проблемы из-за гугл рекламы, блокируется переход на Loader.html
# driver.find_element_by_css_selector('a[href="Loader.html"]').click()

driver.get("http://demo.automationtesting.in/Loader.html")
# явное ожидание для кнопки Run
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[id='loader']"))).click()
# явное ожидание присутствия текста "Lorem" у элемента. На странице нет(!) модального окна - вместо него div
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'div[id="myModal"] p'),"Lorem"))
time.sleep(3) # только чтобы увидеть, можно убрать
# явное ожидание для элемента "Save Changes"
wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@id='myModal']//button[2]"))).click()
driver.quit()
