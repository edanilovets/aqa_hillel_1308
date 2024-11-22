from selenium.webdriver.remote.webdriver import WebDriver

from lesson28.src.pages.element_actions import ElementActions


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.actions = ElementActions(driver)

    def open(self, url: str):
        self.driver.get(url)
