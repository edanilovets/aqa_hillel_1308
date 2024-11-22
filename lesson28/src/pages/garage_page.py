from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from lesson28.src.models.car_model import Car
from lesson28.src.pages.base_page import BasePage
from lesson28.src.custom_expected_conditions import CarToBeAddedToGarage

class GaragePage(BasePage):
    # Modal window for car adding
    ADD_CAR_BTN = (By.CSS_SELECTOR, "app-garage .btn.btn-primary")
    CAR_BRAND_SELECTOR = (By.ID, "addCarBrand")
    CAR_MODEL_SELECTOR = (By.ID, "addCarModel")
    CAR_MILEAGE_INPUT = (By.ID, "addCarMileage")
    CAR_MILEAGE_SELECTOR = (By.ID, "addCarMileage1")
    ADD_BTN = (By.CSS_SELECTOR, ".modal-footer .btn.btn-primary")
    # Modal window for fuel expenses
    # TODO

    def add_car(self, car: Car, wait_time: int = 5):
        """Adding car to the garage"""
        self.actions.click(self.ADD_CAR_BTN)
        brand_el = Select(self.actions.find(self.CAR_BRAND_SELECTOR))
        WebDriverWait(self.driver, wait_time).until(EC.text_to_be_present_in_element(self.CAR_BRAND_SELECTOR, car.brand))
        brand_el.select_by_visible_text(car.brand)
        model_el = Select(self.actions.find(self.CAR_MODEL_SELECTOR))
        WebDriverWait(self.driver, wait_time).until(EC.text_to_be_present_in_element(self.CAR_MODEL_SELECTOR, car.model))
        model_el.select_by_visible_text(car.model)
        self.actions.fill(self.CAR_MILEAGE_INPUT, car.mileage)
        self.actions.click(self.ADD_BTN)
        WebDriverWait(self.driver, wait_time).until(CarToBeAddedToGarage())

    def add_fuel_expense(self):
        pass