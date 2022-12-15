# Вызов и прием alert
# Section 2, module 3, step 4

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

url = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome(executable_path='E:\My_files\Programming\PyProjects\StepikSeleniumCourse\drivers\chromedriver.exe')
browser.get(url=url)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()
    alert = browser.switch_to.alert
    alert.accept()

    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)
    input = browser.find_element(By.ID, 'answer')
    input.send_keys(y)
    submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit.click()

finally:
    time.sleep(4)
    browser.close()
    browser.quit()