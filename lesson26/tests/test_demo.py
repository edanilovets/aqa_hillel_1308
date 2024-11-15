from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

# Search strategies
# ID = "id"
# XPATH = "xpath"
# LINK_TEXT = "link text"
# PARTIAL_LINK_TEXT = "partial link text"
# NAME = "name"
# TAG_NAME = "tag name"
# CLASS_NAME = "class name"
# CSS_SELECTOR = "css selector"

def test_demo():
    driver = Chrome()
    driver.get("http://localhost:8000/src/demo.html")

    # By.XPATH

    # find_element -> WebElement
    user_field = driver.find_element(By.ID, "username")
    pass_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login_button")

    form_element = driver.find_element(By.TAG_NAME, "form")

    # find_elements -> list[WebElement]
    user_fields = driver.find_elements(By.ID, "username")

    # WebElement -> find_element
    # user_field.find_element()

    li_elements = driver.find_elements(By.TAG_NAME, "li")

    for li in li_elements:
        if li.text == "Елемент списку 2":
            print("Знайдено елемент:", li.text)
            break

    driver.quit()

