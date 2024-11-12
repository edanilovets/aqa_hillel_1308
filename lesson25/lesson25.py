# xpath, css, re

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com/")

search_form = driver.find_element(By.XPATH, "//*[@name='q']")  # return WebElement
print("Search aria-label:", search_form.get_attribute("aria-label"))

logo = driver.find_element(By.CSS_SELECTOR, "div#gb a.gb_A.gb_Xa.gb_Z")
logo_image = logo.find_element(By.TAG_NAME, "img")
print("Logo image class:", search_form.get_attribute("innerHTML"))