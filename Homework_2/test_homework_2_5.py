import pytest
from selenium.webdriver.common.by import By


@pytest.mark.basic
def test_typos(browser):

    # Обозначаем УРЛ
    browser.get("https://the-internet.herokuapp.com/typos")

    # Проверяем текст до 10 попыток
    text_found = False

    for i in range(10):
        Test = browser.find_element(By.XPATH, "//p[2]")
        if Test.text == "Sometimes you'll see a typo, other times you won't.":
            text_found = True
            print(f"Правильный текст найден. Попытка {i + 1}")
            break

        browser.refresh()

    assert text_found, "Отсутствует нужный результат за 10 попыток"