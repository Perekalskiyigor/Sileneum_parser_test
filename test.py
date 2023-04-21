from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
try:
    driver.get("https://finecooking.ru/")
    # name_input = driver.find_element(By.NAME, "email")
    # name_input =driver.find_element(By.ID, "id")
    # name_input =driver.find_element(By.NAME, "name")
    # name_input =driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/main/div[2]/div[11]/div/div[1]")
    name_input =driver.find_element(By.LINK_TEXT, "Регистрация")
    name_input.click()
    input()
    name_input2 =driver.find_element(By.XPATH, '//*[@id="register-form"]/div[1]/input')
    name_input2.send_keys("123")
    input()
    name_input2.submit()
    input()
    # name_input =driver.find_element(By.PARTIAL_LINK_TEXT, "partial link text")
    # name_input =driver.find_element(By.TAG_NAME, "h1")
    # name_input =driver.find_elements(By.CLASS_NAME, "caption recipe-block-name")
    # name_input =driver.find_element(By.CSS_SELECTOR, "css selector")
    # print(f"найден {name_input.text}")
    #print(f"найден {name_input.location}")
    # for e in name_input:
    #    print(f"1 = {e.text}")
except:
    print("не найден")
