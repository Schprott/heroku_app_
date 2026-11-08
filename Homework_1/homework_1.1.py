# Импортируем опции селениума
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# Прокидываем нужные настройки
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")

# Обозначаем УРЛ
driver = webdriver.Chrome(options=options)
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

# Обозначаем нужные элементы и действия с ними
add_element = driver.find_element(By.XPATH, "//button[text()='Add Element']")
add_element.click()
add_element.click()

delete_elements = driver.find_elements(By.XPATH, "//button[text()='Delete']")
# Проверяем количество элементов Delete
assert len(delete_elements) == 2

delete_elements[0].click()
delete_elements = driver.find_elements(By.XPATH, "//button[text()='Delete']")

# Проверяем количество элементов Delete после удаления
assert len(delete_elements) == 1


driver.quit()