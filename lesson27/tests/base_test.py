from selenium.webdriver.remote.webdriver import WebDriver

from lesson27.src.pages.main_page import MainPage
from lesson27.src.utils.settings_reader import SettingsReader


class BaseTest:
    settings = SettingsReader()
    url = settings.get_base_ui_url()

    def login_as_guest(self, driver: WebDriver):
        main_page = MainPage(driver)
        main_page.open(self.url)
        main_page.click_guest_login()

    def login(self, username: str, password: str):
        pass