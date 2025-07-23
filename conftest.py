import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Credentials
from locators import LoginPageLocators, MainPageLocators
from urls import Urls

# Fixture для настройки окружения тестов
@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1280,1024")
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

# Fixture для авторизации пользователя
@pytest.fixture
def login(driver):
    driver.get(Urls.URL_MAIN_PAGE)
    driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
    ).send_keys(Credentials.email)

    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(Credentials.password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_LINK)
    )
    return driver
