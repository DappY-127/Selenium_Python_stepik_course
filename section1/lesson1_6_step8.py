# Поиск элемента по XPath
# Section 1, module 6, step 8

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'http://suninjuly.github.io/find_xpath_form'

try:
    browser = webdriver.Chrome(executable_path='')
    browser.get(url=url)
    firstNameInput = browser.find_element(By.XPATH, '//input[@name="first_name"]')
    lastNameInput = browser.find_element(By.XPATH, '//input[@name="last_name"]')
    cityInput = browser.find_element(By.XPATH, '')
    countryInput = browser.find_element(By.XPATH, '')

    submitBttn = browser.find_element(By.XPATH, "//button[@type='submit']")
    submitBttn.click()

finally:
    time.sleep(4)
    browser.close()
    browser.quit()