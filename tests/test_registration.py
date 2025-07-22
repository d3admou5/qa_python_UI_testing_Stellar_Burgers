from locators import RegistrationLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from user_generator import generate_registration_data

# Регистрация с валидными данными
def test_successful_registration(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")

    name, email, password = generate_registration_data(password_length=8)

    driver.find_element(*RegistrationLocators.NAME_INPUT).send_keys(name)
    driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegistrationLocators.REGISTER_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.url_contains("/login"))
    assert "/login" in driver.current_url

# Регистрация с коротким паролем
def test_short_password_error(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")

    name, email, password = generate_registration_data(password_length=5)  # короткий пароль

    driver.find_element(*RegistrationLocators.NAME_INPUT).send_keys(name)
    driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegistrationLocators.REGISTER_BUTTON).click()

    error_element = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(RegistrationLocators.ERROR_HINT)
    )
    assert "Некорректный пароль" in error_element.text

    try:
        WebDriverWait(driver, 3).until(EC.url_contains("/login"))
        redirected = True
    except TimeoutException:
        redirected = False

    assert not redirected
