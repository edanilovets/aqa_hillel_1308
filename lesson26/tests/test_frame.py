from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_frame():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/src/scroll_frame.html")

    # execute_script
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)

    frame_element = driver.find_element(By.ID, "myFrame")
    driver.switch_to.frame(frame_element)

    for _ in range(3):
        button = driver.find_element(By.ID, "myButton")
        button.click()
        time.sleep(1)

    driver.switch_to.default_content()
    main_page_title = driver.find_element(By.TAG_NAME, "h1")
    assert main_page_title.text == "Main Page"

    driver.quit()

