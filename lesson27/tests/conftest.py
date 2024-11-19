import pytest
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture(scope="session")
def driver():
    # setup
    options = ChromeOptions()
    options.add_argument("--incognito")
    # options.add_argument("--headless")
    driver = Chrome(options=options)
    # driver = SetupDriver()
    driver.maximize_window()
    yield driver
    # teardown
    driver.quit()
