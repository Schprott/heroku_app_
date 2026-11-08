import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@pytest.mark.basic
def test_inputs(browser):

    # Обозначаем УРЛ
    browser.get("https://the-internet.herokuapp.com/inputs")

    input_form = browser.find_element(By.TAG_NAME, "input")
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

    # Проверяем работу клавиши вниз
    input_form.send_keys(Keys.ARROW_DOWN)
    assert input_form.get_attribute("value") == "1"
    input_form.clear()

    input_form.send_keys("9")
    assert input_form.get_attribute("value") == "9"

    # Проверяем работу клавиши вверх
    input_form.send_keys(Keys.ARROW_UP)
    assert input_form.get_attribute("value") == "10"