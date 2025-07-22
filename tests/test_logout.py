from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Credentials
from locators import MainPageLocators, LoginPageLocators, ProfilePageLocators

# Тест на выход из профиля
def test_logout_from_profile(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(Credentials.email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(Credentials.password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_LINK)).click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ProfilePageLocators.LOGOUT_BUTTON)).click()

    WebDriverWait(driver, 5).until(EC.url_contains("/login"))
    assert "/login" in driver.current_url
