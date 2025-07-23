import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators import RegistrationLocators
from helpers.user_generator import generate_registration_data
from urls import Urls
from helpers.registration_form import fill_registration_form

# Тест для проверки регистрации пользователя
class TestRegistration:
    def test_successful_registration(self, driver):
        driver.get(Urls.URL_REGISTER)
        name, email, password = generate_registration_data(password_length=8)
        fill_registration_form(driver, name, email, password)

        WebDriverWait(driver, 10).until(EC.url_contains("/login"))

        assert "/login" in driver.current_url, \
            f"После успешной регистрации ожидался переход на /login, но URL: {driver.current_url}"

# Тест на ввод короткого пароля
    def test_short_password_error(self, driver):
        driver.get(Urls.URL_REGISTER)
        name, email, password = generate_registration_data(password_length=5)
        fill_registration_form(driver, name, email, password)

        error_element = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(RegistrationLocators.ERROR_HINT))

        assert "Некорректный пароль" in error_element.text

        with pytest.raises(TimeoutException):
            WebDriverWait(driver, 3).until(EC.url_changes(driver.current_url))


# Отделил функцию в отдельный файл helpers/registration_form.py. Чтобы улучшить читаемость