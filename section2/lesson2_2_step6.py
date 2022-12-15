# Использование execute_script
# Section 2, module 2, step 6

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

url = 'https://suninjuly.github.io/execute_script.html'
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome(executable_path='E:\My_files\Programming\PyProjects\StepikSeleniumCourse\drivers\chromedriver.exe')
    browser.get(url=url)
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    inputField = browser.find_element(By.ID, 'answer')
    inputField.send_keys(y)
    submitBttn = browser.find_element(By.CSS_SELECTOR, '.btn')
    browser.execute_script("return arguments[0].scrollIntoView(true);", submitBttn)   
    robotCheck = browser.find_element(By.ID, 'robotCheckbox')
    robotCheck.click()  
    robotRadio = browser.find_element(By.ID, 'robotsRule')
    robotRadio.click()
    
    submitBttn.click()

finally:
    time.sleep(4)
    browser.close()
    browser.quit()

