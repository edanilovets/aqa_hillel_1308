from selenium.webdriver.remote.webdriver import WebDriver

from lesson28.src.pages.element_actions import ElementActions


class BasePage:
    def __init__(self, driver: WebDriver, auto_config: dict):
        self.driver = driver
        self.auto_config = auto_config
        self.base_url = auto_config.get("base_url_ui")
        self.actions = ElementActions(driver)
