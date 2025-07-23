from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, ProfilePageLocators
from urls import Urls

# Тесты на выход из профиля
def test_logout_from_profile(driver, login):
    driver.get(Urls.URL_MAIN_PAGE)
    driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
    login()  # фикстура авторизации

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)).click()

    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(ProfilePageLocators.LOGOUT_BUTTON)).click()

    WebDriverWait(driver, 5).until(EC.url_contains("/login"))

    assert "/login" in driver.current_url, f"После выхода ожидался редирект на /login, но сейчас: {driver.current_url}"
