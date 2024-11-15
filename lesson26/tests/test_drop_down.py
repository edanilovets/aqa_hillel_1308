import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_drop_down():
    driver = Chrome()
    driver.get("http://localhost:8000/src/drop_down_menu.html")

    actions = ActionChains(driver)

    time.sleep(1)
    menu_button = driver.find_element(By.TAG_NAME, "button")

    actions.move_to_element(menu_button).perform()

    product_links = driver.find_elements(By.CSS_SELECTOR, ".dropdown-submenu .dropdown-content .product-link")

    for link in product_links:
        actions.move_to_element(link).perform()
        actions.click(link).perform()
        time.sleep(1)
        # driver.click(catalog)
        # wait for notebooks to be displayed
        # driver.click(notebooks)
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        time.sleep(1)
        alert = driver.switch_to.alert
        alert.accept()

    driver.quit()
