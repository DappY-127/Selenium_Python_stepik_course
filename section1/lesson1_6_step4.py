# Поиск элементов с помощью Selenium.
# Нужно открыть страницу по ссылке и заполнить форму на этой странице с помощью Selenium.
# Section 1, module 6, step 4

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome(executable_path='E:\My_files\Programming\PyProjects\StepikSeleniumCourse\drivers\chromedriver.exe')
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys('Ryan')
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys('Gosling')
    input3 = browser.find_element(By.CLASS_NAME, 'city')
    input3.send_keys('Bahmut')
    input4 = browser.find_element(By.ID, 'country')
    input4.send_keys('Ukraine')

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

finally:
    time.sleep(5)
    browser.close()
    browser.quit()
