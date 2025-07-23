import pytest
from urls import Urls
from locators import ConstructorPageLocators
from helpers.constructor_actions import click_and_wait_for_tab


class TestConstructorTabs:

    @pytest.mark.parametrize("tab_locator, expected_text", [
        (ConstructorPageLocators.SAUCES_TAB, "Соусы"),
        (ConstructorPageLocators.FILLINGS_TAB, "Начинки"),
        (ConstructorPageLocators.BUNS_TAB, "Булки"),
    ])
    def test_constructor_tab_switch(self, driver, tab_locator, expected_text):
        driver.get(Urls.URL_MAIN_PAGE)
        click_and_wait_for_tab(driver, tab_locator, expected_text)
