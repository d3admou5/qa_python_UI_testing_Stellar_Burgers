from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Credentials
from locators import MainPageLocators, LoginPageLocators, ProfilePageLocators

def test_go_to_personal_account(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Клик по кнопке "Войти в аккаунт" на главной
    driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

    # Заполнение формы логина
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(Credentials.email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(Credentials.password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    # Ожидание перехода после логина
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_LINK))

    # Клик по "Личный кабинет"
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()

    # Проверка, что открыта страница профиля
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ProfilePageLocators.LOGOUT_BUTTON))
    assert "account/profile" in driver.current_url
