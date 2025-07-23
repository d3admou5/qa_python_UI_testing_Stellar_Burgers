import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from locators import ConstructorPageLocators
from urls import Urls

# Тесты для переключения вкладок в конструкторе бургеров
class TestConstructorTabs:
    def click_and_wait_for_tab(self, driver, tab_locator, expected_text, timeout=5):

        tab = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(tab_locator)
        )

        driver.execute_script("arguments[0].scrollIntoView(true);", tab)
        time.sleep(0.2)

        actions = ActionChains(driver)
        actions.move_to_element(tab).click().perform()

        WebDriverWait(driver, timeout).until(
            lambda d: d.find_element(*ConstructorPageLocators.ACTIVE_TAB).text.strip() == expected_text
        )

        active_tab = driver.find_element(*ConstructorPageLocators.ACTIVE_TAB).text.strip()
        assert active_tab == expected_text, f"Ожидалась активная вкладка '{expected_text}', но была '{active_tab}'"

# Тесты для переключения вкладок в конструкторе бургеров
    @pytest.mark.parametrize("tab_locator, expected_text", [
        (ConstructorPageLocators.SAUCES_TAB, "Соусы"),
        (ConstructorPageLocators.FILLINGS_TAB, "Начинки"),
        (ConstructorPageLocators.BUNS_TAB, "Булки"),
    ])
    def test_constructor_tab_switch(self, driver, tab_locator, expected_text):
        driver.get(Urls.URL_MAIN_PAGE)
        self.click_and_wait_for_tab(driver, tab_locator, expected_text)
