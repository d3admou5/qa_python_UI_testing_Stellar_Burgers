from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_constructor_tabs(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")

    wait = WebDriverWait(driver, 5)

    # Вкладки
    buns_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Булки']")))
    sauces_tab = driver.find_element(By.XPATH, "//span[text()='Соусы']")
    fillings_tab = driver.find_element(By.XPATH, "//span[text()='Начинки']")

    # Клик на "Соусы" и проверка
    sauces_tab.click()
    active_tab = driver.find_element(By.CLASS_NAME, "tab_tab_type_current__2BEPc")
    assert active_tab.text == "Соусы"

    # Клик на "Начинки" и проверка
    fillings_tab.click()
    active_tab = driver.find_element(By.CLASS_NAME, "tab_tab_type_current__2BEPc")
    assert active_tab.text == "Начинки"

    # Клик обратно на "Булки" и проверка
    buns_tab.click()
    active_tab = driver.find_element(By.CLASS_NAME, "tab_tab_type_current__2BEPc")
    assert active_tab.text == "Булки"
