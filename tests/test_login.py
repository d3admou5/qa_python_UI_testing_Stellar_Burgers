from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import Urls
from data import Credentials
from locators import MainPageLocators, LoginPageLocators, RegisterPageLocators


# Вход по кнопке «Войти в аккаунт» на главной
def test_login_from_main_page(driver):
    driver.get(Urls.URL_MAIN_PAGE)
    driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(Credentials.email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(Credentials.password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_LINK))
    assert driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).is_displayed(), \
        "Не отображается ссылка на личный кабинет после входа с главной страницы"


# Вход через кнопку «Личный кабинет»
def test_login_from_personal_account_button(driver):
    driver.get(Urls.URL_MAIN_PAGE)
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(Credentials.email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(Credentials.password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_LINK))
    assert driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).is_displayed(), \
        "Не отображается ссылка на личный кабинет после входа через кнопку 'Личный кабинет'"

# Вход через кнопку в форме регистрации
def test_login_from_register_page(driver):
    driver.get(Urls.URL_REGISTER)
    driver.find_element(*RegisterPageLocators.LOGIN_LINK).click()  # переход на форму входа

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(Credentials.email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(Credentials.password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_LINK))
    assert driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).is_displayed(), \
        "Не отображается ссылка на личный кабинет после входа через форму регистрации"


# Вход через кнопку в форме восстановления пароля
def test_login_from_forgot_password_page(driver):
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
    driver.find_element(*RegisterPageLocators.LOGIN_LINK).click()  # переход на форму входа

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(Credentials.email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(Credentials.password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_LINK))
    assert driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).is_displayed(), \
        "Не отображается ссылка на личный кабинет после входа через форму восстановления пароля"
