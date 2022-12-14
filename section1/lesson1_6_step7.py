# Использование метода find_elements
# Section 1, module 6, step 7

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'http://suninjuly.github.io/huge_form.html'

try:
    browser = webdriver.Chrome(executable_path='E:\My_files\Programming\PyProjects\StepikSeleniumCourse\drivers\chromedriver.exe')
    browser.get(url=url)
    fields = browser.find_elements(By.TAG_NAME, 'input')
    for field in fields:
        field.send_keys('bruh')
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()    

finally:
    time.sleep(4)
    browser.close()
    browser.quit()

