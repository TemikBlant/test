from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from pages import MainPage

def get_driver():
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    browser = webdriver.Chrome(options=options)
    return browser


@pytest.fixture()
def open_stackoverflow():
    browser_driver = get_driver()
    browser_driver.get("https://stackoverflow.com/")
    yield browser_driver
    browser_driver.quit()


@pytest.fixture()
def go_login_stackoverflow(open_stackoverflow):
    MainPage(open_stackoverflow).log_in_button_click()
    yield open_stackoverflow
