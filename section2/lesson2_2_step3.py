# Работа с выпадающим списком
# Section 2, module 2, step 3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

url1 = 'http://suninjuly.github.io/selects1.html'
url2 = 'http://suninjuly.github.io/selects2.html'

try:
    browser = webdriver.Chrome(executable_path='E:\My_files\Programming\PyProjects\StepikSeleniumCourse\drivers\chromedriver.exe')
    browser.get(url=url1)
    num1 = browser.find_element(By.ID, 'num1').text
    num2 = browser.find_element(By.ID, 'num2').text
    answer = int(num1) + int(num2)
    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_value(str(answer))

    browser.find_element(By.TAG_NAME, 'button').click()

finally:
    time.sleep(4)
    browser.close()
    browser.quit()    

