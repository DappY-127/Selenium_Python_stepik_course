# Регистрация на сайте, заполнив только обязательные поля, отмеченные символом *.
# Успешность регистрации проверяется сравнением ожидаемого текста с текстом на странице, которая открывается после регистрации. 
# Для сравнения используеться стандартная конструкция assert из Python.
# Section 1, module 6, step 10

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome(executable_path='E:\My_files\Programming\PyProjects\StepikSeleniumCourse\drivers\chromedriver.exe')
    browser.get(url='http://suninjuly.github.io/registration1.html')

    reqFirstNameField = browser.find_element(By.CSS_SELECTOR, '.form-control.first:required')
    reqFirstNameField.send_keys('Name')
    reqSecondNameField = browser.find_element(By.CSS_SELECTOR, '.form-control.second:required')
    reqSecondNameField.send_keys('Surname')
    reqMailField = browser.find_element(By.CSS_SELECTOR, '.form-control.third:required')
    reqMailField.send_keys('kek@mail')

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
   
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(4)
    browser.close()
    browser.quit()

