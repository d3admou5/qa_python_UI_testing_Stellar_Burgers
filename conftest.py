import pytest
from selenium import webdriver
from data import Credentials

# Фикстура для браузера
@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1280,1024")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)  # можно изменить или убрать, если используешь WebDriverWait
    yield driver
    driver.quit()

# Фикстура с данными пользователя
@pytest.fixture
def test_user():
    return {
        "email": Credentials.email,
        "password": Credentials.password,
    }

