# Поиск элемента по XPath + использование метода find_elements для заполнения форм
# Section 1, module 6, step 8

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'http://suninjuly.github.io/find_xpath_form'
answers = ['Name', 'Surname', 'Kyiv', 'Ukraine']

try:
    browser = webdriver.Chrome(executable_path='E:\My_files\Programming\PyProjects\StepikSeleniumCourse\drivers\chromedriver.exe')
    browser.get(url=url)
    inputs = browser.find_elements(By.XPATH, '//input')
    i = 0
    for input in inputs:
        input.send_keys(answers[i])
        i += 1

    submitBttn = browser.find_element(By.XPATH, "//button[@type='submit']")
    submitBttn.click()

finally:
    time.sleep(4)
    browser.close()
    browser.quit()