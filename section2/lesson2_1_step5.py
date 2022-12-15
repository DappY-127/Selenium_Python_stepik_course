# Кликаем по checkboxes и radiobuttons
# Section 2, module 1, step 5

import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://suninjuly.github.io/math.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))) 

try:
    browser = webdriver.Chrome(executable_path='E:\My_files\Programming\PyProjects\StepikSeleniumCourse\drivers\chromedriver.exe')
    browser.get(url=url)
    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)
    input = browser.find_element(By.ID, 'answer')
    input.send_keys(y)
    check = browser.find_element(By.ID, 'robotCheckbox')
    check.click()
    radio = browser.find_element(By.ID, 'robotsRule')
    radio.click()
    submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit.click()
    

finally:
    time.sleep(4)
    browser.close()
    browser.quit()    