from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
import time

def test_dialog():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/src/dialog.html")

    driver.find_element(By.XPATH, "//button[text()='Показати Alert']").click()
    alert = Alert(driver)
    print("Текст Alert:", alert.text)
    alert.accept()

    driver.find_element(By.XPATH, "//button[text()='Показати Confirm']").click()
    alert = Alert(driver)
    print("Текст Confirm:", alert.text)
    alert.accept()

    driver.find_element(By.XPATH, "//button[text()='Показати Prompt']").click()
    alert = Alert(driver)
    print("Текст Prompt:", alert.text)
    alert.send_keys("John")
    alert.accept()

    time.sleep(2)

    driver.quit()

