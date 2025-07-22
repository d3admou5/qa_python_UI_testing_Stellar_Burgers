from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Credentials
from locators import MainPageLocators, LoginPageLocators
from urls import Urls


# Вспомогательная функция для авторизации
def login(driver):
    driver.get(Urls.URL_MAIN_PAGE)
    driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
    ).send_keys(Credentials.email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(Credentials.password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_LINK)
    )


# Тест на переход в личный кабинет
def test_go_to_personal_account(driver):
    login(driver)
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()
    assert "/account" in driver.current_url, \
        f"Ожидался переход в личный кабинет, но URL: {driver.current_url}"


# Тест на переход из профиля в конструктор по кнопке
def test_go_from_profile_to_constructor(driver):
    login(driver)
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()
    driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()

    WebDriverWait(driver, 5).until(
        EC.url_to_be(Urls.URL_MAIN_PAGE)
    )
    assert driver.current_url == Urls.URL_MAIN_PAGE, \
        f"Ожидался переход на главную, но URL: {driver.current_url}"


# Тест на переход из профиля в конструктор по логотипу
def test_go_to_constructor_by_logo(driver):
    login(driver)
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()
    driver.find_element(*MainPageLocators.LOGO_BUTTON).click()

    WebDriverWait(driver, 5).until(
        EC.url_to_be(Urls.URL_MAIN_PAGE)
    )
    assert driver.current_url == Urls.URL_MAIN_PAGE, \
        f"Ожидался переход на главную, но URL: {driver.current_url}"
