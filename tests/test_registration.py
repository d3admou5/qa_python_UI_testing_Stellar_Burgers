import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators import RegistrationLocators
from user_generator import generate_registration_data
from urls import Urls

class TestRegistration:
# Метод для заполнения формы регистрации
    def fill_registration_form(self, driver, name, email, password):
        driver.find_element(*RegistrationLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationLocators.REGISTER_BUTTON).click()

# Тест на успешную регистрацию
    def test_successful_registration(self, driver):
        driver.get(Urls.URL_REGISTER)

        name, email, password = generate_registration_data(password_length=8)
        self.fill_registration_form(driver, name, email, password)

        WebDriverWait(driver, 10).until(EC.url_contains("/login"))
        assert "/login" in driver.current_url, \
            f"После успешной регистрации ожидался переход на /login, но URL: {driver.current_url}"

# Тест на ввод короткого пароля
    def test_short_password_error(self, driver):
        driver.get(Urls.URL_REGISTER)

        name, email, password = generate_registration_data(password_length=5)
        self.fill_registration_form(driver, name, email, password)

        error_element = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(RegistrationLocators.ERROR_HINT)
        )
        assert "Некорректный пароль" in error_element.text

        with pytest.raises(TimeoutException):
            WebDriverWait(driver, 3).until(EC.url_changes(driver.current_url))
