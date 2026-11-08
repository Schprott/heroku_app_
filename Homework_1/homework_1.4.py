# Импортируем опции селениума
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# Прокидываем нужные настройки
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")

# Обозначаем УРЛ
driver = webdriver.Chrome(options=options)
driver.get("https://the-internet.herokuapp.com/inputs")
input_form = driver.find_element(By.TAG_NAME, "input")
input_form.send_keys("-10")
assert input_form.get_attribute("value") == "-10"
# Очищаем поле
input_form.clear()

# Проверяем на буквы
input_form.send_keys("OK")
assert input_form.get_attribute("value") == ""
input_form.clear()

input_form.send_keys("2")
assert input_form.get_attribute("value") == "2"
# Проверяем на работу клавиши вниз
input_form.send_keys(Keys.ARROW_DOWN)
assert input_form.get_attribute("value") == "1"
input_form.clear()

input_form.send_keys("9")
assert input_form.get_attribute("value") == "9"
# Проверяем на работу клавиши вверх
input_form.send_keys(Keys.ARROW_UP)
assert input_form.get_attribute("value") == "10"

driver.quit()