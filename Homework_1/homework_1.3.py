# Импортируем опции селениума
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


# Прокидываем нужные настройки
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")

# Обозначаем УРЛ
driver = webdriver.Chrome(options=options)
driver.get("https://the-internet.herokuapp.com/dropdown")

# Проверяем наличие всех элементов
dropdown = driver.find_element(By.ID, "dropdown")
select = Select(dropdown)
option_text = [option.text for option in select.options]
assert option_text[0] == "Please select an option"
assert option_text[1] == "Option 1"
assert option_text[2] == "Option 2"

# Выбираем элемент
select.select_by_index(1)
# Проверяем что он выбран
assert select.first_selected_option.text == "Option 1"
# Выбираем элемент номер 2
select.select_by_index(2)
# Проверяем что он выбран
assert select.first_selected_option.text == "Option 2"


driver.quit()