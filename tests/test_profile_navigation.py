from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Credentials
from locators import MainPageLocators, LoginPageLocators

# Тест на переход в личный кабинет
def test_go_to_personal_account(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(Credentials.email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(Credentials.password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_LINK))

    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()

    assert "/account" in driver.current_url

# Тест на переход из профиля в конструктор
def test_go_from_profile_to_constructor(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(Credentials.email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(Credentials.password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_LINK))

    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()

    driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()

    WebDriverWait(driver, 5).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

# Тест на переход в конструктор по логотипу
def test_go_to_constructor_by_logo(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(Credentials.email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(Credentials.password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_LINK))
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()

    driver.find_element(*MainPageLocators.LOGO_BUTTON).click()

    WebDriverWait(driver, 5).until(EC.url_matches("https://stellarburgers.nomoreparties.site/"))
    assert "stellarburgers.nomoreparties.site" in driver.current_url
