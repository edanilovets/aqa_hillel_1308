from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
import time

def test_elements():
    driver = Chrome()
    driver.get("http://localhost:8000/src/action_chains.html")

    circle = driver.find_element(By.ID, "circle")
    actions = ActionChains(driver)
    zone = driver.find_element(By.ID, "container")
    azw = zone.size['width'] - circle.size['width'] - 10
    azh = zone.size['height'] - circle.size['height'] - 10

    try:
        actions.click_and_hold(circle).move_to_element(zone).perform()
        time.sleep(1)
        actions.move_to_element(circle).move_by_offset(azw / 2, azh / 2).perform()
        time.sleep(1)
        actions.move_to_element(circle).move_by_offset(0, -azh).perform()
        time.sleep(1)
        actions.move_to_element(circle).move_by_offset(-azw, 0).perform()
        time.sleep(1)
        actions.move_to_element(circle).move_by_offset(0, azh).perform()
        time.sleep(1)
        actions.click_and_hold(circle).move_to_element(zone).perform()
        time.sleep(1)
        actions.double_click(circle).perform()
        time.sleep(1)
        actions.click(circle).perform()
        time.sleep(1)

        background_color = circle.value_of_css_property("background-color")
        if background_color == "rgba(0, 128, 0, 1)":
            print("Фон змінився на зелений!")

        actions.move_by_offset(-100, -100).perform()
        time.sleep(1)

        background_color_out = circle.value_of_css_property("background-color")
        if background_color_out == "rgba(255, 0, 0, 1)":
            print("Фон змінився на червоний!")

        actions.send_keys(Keys.ENTER).perform()
        time.sleep(1)
        alert = Alert(driver)
        alert.accept()
        time.sleep(0.5)
    finally:
        driver.quit()

