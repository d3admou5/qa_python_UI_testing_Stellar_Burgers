from urls import Urls
from locators import MainPageLocators, RegisterPageLocators

# Вход по кнопке «Войти в аккаунт» на главной
def test_login_from_main_page(driver, login):
    driver.get(Urls.URL_MAIN_PAGE)
    driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
    login() # фикстура авторизации
    assert driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).is_displayed(), \
        "Не отображается ссылка на личный кабинет после входа с главной страницы"

# Вход через кнопку «Личный кабинет»
def test_login_from_personal_account_button(driver, login):
    driver.get(Urls.URL_MAIN_PAGE)
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()
    login() # фикстура авторизации

    assert driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).is_displayed(), \
        "Не отображается ссылка на личный кабинет после входа через кнопку 'Личный кабинет'"

# Вход через кнопку в форме регистрации
def test_login_from_register_page(driver, login):
    driver.get(Urls.URL_REGISTER)
    driver.find_element(*RegisterPageLocators.LOGIN_LINK).click()
    login() # фикстура авторизации

    assert driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).is_displayed(), \
        "Не отображается ссылка на личный кабинет после входа через форму регистрации"

# Вход через кнопку в форме восстановления пароля
def test_login_from_forgot_password_page(driver, login):
    driver.get(Urls.URL_FORGOT_PASSWORD)
    driver.find_element(*RegisterPageLocators.LOGIN_LINK).click()
    login() # фикстура авторизации

    assert driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).is_displayed(), \
        "Не отображается ссылка на личный кабинет после входа через форму восстановления пароля"
