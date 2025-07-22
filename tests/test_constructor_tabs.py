from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import ConstructorPageLocators


def click_and_wait_for_tab(driver, tab_locator, expected_text, timeout=5):
    WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(tab_locator)
    ).click()

    WebDriverWait(driver, timeout).until(
        lambda d: d.find_element(*ConstructorPageLocators.ACTIVE_TAB).text == expected_text
    )

    active_tab = driver.find_element(*ConstructorPageLocators.ACTIVE_TAB).text
    assert active_tab == expected_text, f"Ожидалась активная вкладка '{expected_text}', но была '{active_tab}'"


def test_constructor_tabs(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Переключаемся на "Соусы"
    click_and_wait_for_tab(driver, ConstructorPageLocators.SAUCES_TAB, "Соусы")

    # Переключаемся на "Начинки"
    click_and_wait_for_tab(driver, ConstructorPageLocators.FILLINGS_TAB, "Начинки")

    # Переключаемся на "Булки"
    click_and_wait_for_tab(driver, ConstructorPageLocators.BUNS_TAB, "Булки")
