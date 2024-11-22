from lesson28.src.models.car_model import Car
from lesson28.src.pages.garage_page import GaragePage
from lesson28.tests.base_test import BaseTest


class TestGaragePage(BaseTest):
    def test_add_car(self, driver):
        # Set pages
        garage_page = GaragePage(driver)
        # Login as guest
        self.login_as_guest(driver)
        # Add car
        car1 = Car(brand="Porsche", model="Cayenne", mileage=1000)
        car2 = Car(brand="Audi", model="Q7", mileage=19999)
        garage_page.add_car(car1)
        garage_page.add_car(car2)

        # Verify added car
        # TODO: assertions
        # garage_page.assert_that_car_was_added(car1)
        # garage_page.assert_that_car_was_added(car2)
