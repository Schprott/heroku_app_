import pytest
from selenium.webdriver.common.by import By

# Добавляем заготовленный файл с функциями из conftest
@pytest.mark.basic
def test_checkboxes(browser):

    # Обозначаем УРЛ
    browser.get("https://the-internet.herokuapp.com/checkboxes")

    # Проверяем чек-боксы
    checkbox_1 = browser.find_element(By.XPATH, "//input[1]")
    checkbox_2 = browser.find_element(By.XPATH, "//input[2]")

    # Проверяем состояние чек-боксов
    assert checkbox_1.is_selected() == False
    assert checkbox_2.is_selected() == True

    # Включаем/выключаем чек-боксы
    checkbox_1.click()
    checkbox_2.click()

    # Проверяем состояние чек-боксов
    assert checkbox_1.is_selected() == True
    assert checkbox_2.is_selected() == False