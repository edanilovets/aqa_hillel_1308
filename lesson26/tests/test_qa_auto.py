from selenium.webdriver.common.by import By


class TestQaAuto:
    def test_add_car(self, driver):
        driver.get("https://guest:welcome2qauto@qauto2.forstudy.space")
        # Open Guest Login
        guest_login_btn = driver.find_element(By.CSS_SELECTOR, "button.header-link.-guest")
        assert guest_login_btn.text == "Guest log in"
        guest_login_btn.click()
        # Add car
        driver.find_element(By.CSS_SELECTOR, "app-garage .btn.btn-primary").click()
        # TODO:
        # Verify added car
