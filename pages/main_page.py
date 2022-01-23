from locators.main import Header
from pages.base_page import BasePage


class MainPage(BasePage):

    def log_in_button_click(self):
        return self._click(Header.log_in_button)
