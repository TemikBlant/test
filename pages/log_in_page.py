from locators.log_in import Log_In
from .base_page import BasePage
import allure


class LogInPage(BasePage):

    def email_input(self, email):
        with allure.step(f'Input {email} in email field'):
            return self._input(Log_In.email_field, email)

    def password_input(self, password):
        with allure.step(f'Input {password} in password field'):
            return self._input(Log_In.password_field, password)

    def submit_button_click(self):
        with allure.step(f'Click to submit button'):
            return self._click(Log_In.submit_button)

    def login(self, email, password):
        self.email_input(email)
        self.password_input(password)
        self.submit_button_click()

    def get_email_error_message(self):
        with allure.step('Get email error message'):
            return self._text(Log_In.email_error_message)

