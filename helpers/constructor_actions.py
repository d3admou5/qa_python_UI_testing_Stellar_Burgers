from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from locators import ConstructorPageLocators

# Функция для клика по вкладке и ожидания её активации с проверкой наличия активного класса
def click_and_wait_for_tab(driver, tab_locator, expected_text, timeout=5):
    tab = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(tab_locator)
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", tab)

    ActionChains(driver).move_to_element(tab).click().perform()

    WebDriverWait(driver, timeout).until(
        lambda d: d.find_element(*ConstructorPageLocators.ACTIVE_TAB).text.strip() == expected_text
    )

    active_tab = driver.find_element(*ConstructorPageLocators.ACTIVE_TAB).text.strip()
    assert active_tab == expected_text, f"Ожидалась активная вкладка '{expected_text}', но была '{active_tab}'"

# Вынес функцию click_and_wait_for_tab в отдельный файл helpers/constructor_actions.py,
# чтобы не дублировать логику клика и ожидания
