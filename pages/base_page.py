from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def __elements(self, locator, index=0):
        by = None
        if 'xpath' in locator.keys():
            by = (By.XPATH, locator['xpath'])
        elif 'id' in locator.keys():
            by = (By.ID, locator['id'])
        elements = WebDriverWait(self.driver, 3).until(EC.visibility_of_all_elements_located(by))
        return elements[index]

    def _element_is_displayed(self, locator):
        return self.__elements(locator).is_displayed()

    def _click(self, locator):
        if self._element_is_displayed(locator):
            return self.__elements(locator).click()

    def _input(self, locator, text, with_clear=True):
        if with_clear:
            self.__elements(locator).clear()
        return self.__elements(locator).send_keys(text)

    def _text(self, locator):
        return self.__elements(locator).text
