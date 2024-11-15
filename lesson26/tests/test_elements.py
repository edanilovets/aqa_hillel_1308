from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def test_elements():
    driver = webdriver.Firefox()
    driver.get("http://localhost:8000/src/elements.html")

    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("example_username")

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("example_password")

    male_radio = driver.find_element(By.ID, "male")
    male_radio.click()

    newsletter_checkbox = driver.find_element(By.ID, "newsletter")
    newsletter_checkbox.click()

    country_dropdown = Select(driver.find_element(By.ID, "country"))
    country_dropdown.select_by_visible_text("США")

    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    time.sleep(5)

    driver.quit()

