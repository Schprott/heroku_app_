import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Добавляем заготовленный файл с функциями из conftest
@pytest.mark.basic
def test_dropdown(browser):

    # Обозначаем УРЛ
    browser.get("https://the-internet.herokuapp.com/dropdown")

    # Проверяем наличие всех элементов
    dropdown = browser.find_element(By.ID, "dropdown")
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

    # Проверяем, что он выбран
    assert select.first_selected_option.text == "Option 2"