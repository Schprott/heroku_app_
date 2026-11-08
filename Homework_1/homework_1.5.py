# Импортируем опции селениума
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# Прокидываем нужные настройки
chrome_options = Options()
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--disable-notifications')

# Обозначаем УРЛ
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://the-internet.herokuapp.com/typos")

# Проводим перебор значений, пока не выйдет нужное
for i in range(10):
    Test = driver.find_element(By.XPATH, "//p[2]")
    assert Test.text == "Sometimes you'll see a typo, other times you won't.", f"Попытка {i + 1}"
    break

time.sleep(3)

driver.quit()
