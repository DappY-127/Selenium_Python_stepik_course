# Регистрация на сайте, заполнив только обязательные поля, отмеченные символом *.
# Успешность регистрации проверяется сравнением ожидаемого текста с текстом на странице, которая открывается после регистрации. 
# Для сравнения используеться стандартная конструкция assert из Python.
# + использование метода find_elements для заполнения форм
# Section 1, module 6, step 10

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome(executable_path='E:\My_files\Programming\PyProjects\StepikSeleniumCourse\drivers\chromedriver.exe')
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    inputs = browser.find_elements(By.CSS_SELECTOR, 'input.form-control:required')
    for input in inputs:
        input.send_keys('required field text')
    

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    # Проверяем, что смогли зарегистрироваться, ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(4)
    browser.close()
    browser.quit()