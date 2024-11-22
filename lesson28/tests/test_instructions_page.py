from lesson28.src.models.car_model import Car
from lesson28.src.pages.instructions_page import InstructionsPage
from lesson28.src.utils.files_utils import FileUtils
from lesson28.tests.base_test import BaseTest
from assertpy import assert_that

class TestInstructionsPage(BaseTest):
    """Test Instructions page"""

    def test_add_car(self, driver, auto_config):
        # Login as guest
        self.login_as_guest(driver, auto_config)
        instructions_page = InstructionsPage(driver, auto_config)
        instructions_page.open()
        car = Car(brand="Audi", model="TT")
        instruction_title = "Front windshield wipers on Audi TT"
        # Click download
        # instructions_page.click_download(instruction_title)
        is_downloaded = FileUtils.wait_for_file_download(f"{instruction_title}.pdf")
        assert_that(is_downloaded).is_true()
