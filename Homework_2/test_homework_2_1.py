import pytest
from selenium.webdriver.common.by import By

# Добавляем заготовленный файл с функциями из conftest
@pytest.mark.basic
def test_add_remove_elements(browser):

    # Обозначаем УРЛ
    browser.get("https://the-internet.herokuapp.com/add_remove_elements/")

    # Обозначаем нужные элементы и действия с ними
    add_element = browser.find_element(By.XPATH, "//button[text()='Add Element']")
    add_element.click()
    add_element.click()

    delete_elements = browser.find_elements(By.XPATH, "//button[text()='Delete']")

    # Проверяем количество элементов Delete
    assert len(delete_elements) == 2

    delete_elements[0].click()
    delete_elements = browser.find_elements(By.XPATH, "//button[text()='Delete']")

    # Проверяем количество элементов Delete после удаления
    assert len(delete_elements) == 1