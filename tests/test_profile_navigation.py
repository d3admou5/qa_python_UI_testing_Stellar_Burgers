from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators
from urls import Urls


class TestNavigationFromAccount:

# Тест на переход в личный кабинет через кнопку "Личный кабинет" в хедере
    def test_go_to_personal_account(self, driver, login):
        driver.get(Urls.URL_LOGIN)  # Сразу на страницу входа
        login() # Фикстура авторизации
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()

        assert "/account" in driver.current_url, \
            f"Ожидался переход в личный кабинет, но URL: {driver.current_url}"

# Тест на переход из личного кабинета обратно в конструктор по кнопке "Конструктор"
    def test_go_from_profile_to_constructor(self, driver, login):
        driver.get(Urls.URL_LOGIN) # Сразу на страницу входа
        login() # Фикстура авторизации
        driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.url_to_be(Urls.URL_MAIN_PAGE))

        assert driver.current_url == Urls.URL_MAIN_PAGE, \
            f"Ожидался переход на главную, но URL: {driver.current_url}"

# Тест на переход из личного кабинета на главную страницу по клику на логотип
    def test_go_to_constructor_by_logo(self, driver, login):
        driver.get(Urls.URL_LOGIN) # Сразу на страницу входа
        login() # Фикстура авторизации
        driver.find_element(*MainPageLocators.LOGO_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.url_to_be(Urls.URL_MAIN_PAGE))

        assert driver.current_url == Urls.URL_MAIN_PAGE, \
            f"Ожидался переход на главную, но URL: {driver.current_url}"
