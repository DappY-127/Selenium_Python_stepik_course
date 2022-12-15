# Переход между вкладками браузера
# Section 2, module 3, step 6

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

url = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome(executable_path='E:\My_files\Programming\PyProjects\StepikSeleniumCourse\drivers\chromedriver.exe')
browser.get(url=url)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:  
    button = browser.find_element(By.CLASS_NAME, 'trollface')
    button.click()
    tabs = browser.window_handles
    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)
    input = browser.find_element(By.ID, 'answer')
    input.send_keys(y)
    submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit.click()


    # browser.switch_to.window(first_window)

finally:
    time.sleep(4)
    browser.close()
    browser.quit()