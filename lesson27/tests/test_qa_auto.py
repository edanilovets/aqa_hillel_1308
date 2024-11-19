from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from lesson27.src.custom_expected_conditions import CarToBeAddedToGarage


class TestQaAuto:
    def test_add_car(self, driver):
        driver.get("https://guest:welcome2qauto@qauto2.forstudy.space")

        guest_login_btn = driver.find_element(By.CSS_SELECTOR, "button.header-link.-guest")
        assert guest_login_btn.text == "Guest log in"
        guest_login_btn.click()

        driver.find_element(By.CSS_SELECTOR, "app-garage .btn.btn-primary").click()
        model_el = Select(WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "addCarBrand"))))
        model_el.select_by_visible_text("Porsche")
        brand_el = Select(WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "addCarModel"))))
        brand_el.select_by_visible_text("Cayenne")
        mileage_input = driver.find_element(By.ID, "addCarMileage")
        mileage_input.send_keys("1000")
        driver.find_element(By.CSS_SELECTOR, ".modal-footer .btn.btn-primary").click()
        WebDriverWait(driver, 5).until(CarToBeAddedToGarage())


        # Verify added car
        # TODO: assertions