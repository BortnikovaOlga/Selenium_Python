# Неявное ожидание поиска элементов.
# должны присутсвовать файлы C:\temp\logotip.png, пустой файл C:\temp\1.txt"
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(7)

img_file = "C:\\temp\\logotip.png"
text_file = "C:\\temp\\1.txt"

driver.get("http://demo.automationtesting.in/FileUpload.html")
# поиск кнопки Browse...
inp_file = driver.find_element_by_css_selector('input[type = "file"]')
# загрузить картинку
inp_file.send_keys(img_file)
# удалить загрузку - нажать кнопку Remove
driver.find_element_by_css_selector('button.fileinput-remove').click()
# загрузить пустой файл
inp_file.send_keys(text_file)
# закрыть сообщение об ошибке
driver.find_element_by_css_selector('span.kv-error-close').click()
# проверка, что кнопка Upload недоступна
upload_btn = driver.find_element_by_css_selector('button.fileinput-upload')
assert upload_btn.get_attribute('disabled')
driver.quit()

