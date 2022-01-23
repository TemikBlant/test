from locators.main import Header
from pages.base_page import BasePage
import allure


class MainPage(BasePage):

    def log_in_button_click(self):
        with allure.step('Click to login button'):
            return self._click(Header.log_in_button)
