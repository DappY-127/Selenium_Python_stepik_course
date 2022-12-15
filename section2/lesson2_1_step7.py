# Использование get_attribute
# Section 2, module 1, step 7

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

url = 'http://suninjuly.github.io/get_attribute.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))) 

try:
    browser = webdriver.Chrome(executable_path='E:\My_files\Programming\PyProjects\StepikSeleniumCourse\drivers\chromedriver.exe')
    browser.get(url=url)
    treasure = browser.find_element(By.ID, 'treasure')
    x = treasure.get_attribute('valuex')
    y = calc(x)
    #try to use another locators (css/xpath)
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