from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
try:
    driver.get("https://www.lambdatest.com")
    # name_input = driver.find_element(By.NAME, "email")
    # name_input =driver.find_element(By.ID, "id")
    # name_input =driver.find_element(By.NAME, "name")
    # name_input =driver.find_element(By.XPATH, "xpath")
    # name_input =driver.find_element(By.LINK_TEXT, "link text")
    # name_input =driver.find_element(By.PARTIAL_LINK_TEXT, "partial link text")
    name_input =driver.find_element(By.TAG_NAME, "h2")
    # name_input =driver.find_element(By.CLASS_NAME, "class name")
    # name_input =driver.find_element(By.CSS_SELECTOR, "css selector")
    print(f"найден {name_input}")
except:
    print("не найден")