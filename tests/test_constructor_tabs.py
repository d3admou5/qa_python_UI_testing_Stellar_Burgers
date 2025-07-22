from selenium.webdriver.support.ui import WebDriverWait
from locators import ConstructorPageLocators

def wait_for_active_tab(driver, expected_text, timeout=5):
    WebDriverWait(driver, timeout).until(
        lambda d: d.find_element(*ConstructorPageLocators.ACTIVE_TAB).text == expected_text
    )

def test_constructor_tabs(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Клик на "Соусы" и ожидание
    driver.find_element(*ConstructorPageLocators.SAUCES_TAB).click()
    wait_for_active_tab(driver, "Соусы")

    # Клик на "Начинки" и ожидание
    driver.find_element(*ConstructorPageLocators.FILLINGS_TAB).click()
    wait_for_active_tab(driver, "Начинки")

    # Клик на "Булки" и ожидание
    driver.find_element(*ConstructorPageLocators.BUNS_TAB).click()
    wait_for_active_tab(driver, "Булки")
