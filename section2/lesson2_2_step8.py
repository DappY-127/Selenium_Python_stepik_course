# Загрузка файла на страницу
# Section 2, module 2, step 8

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

url = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome(executable_path='E:\My_files\Programming\PyProjects\StepikSeleniumCourse\drivers\chromedriver.exe')
browser.get(url=url)

try:
    inputs = browser.find_elements(By.CSS_SELECTOR, '.form-control')
    for input in inputs:
        input.send_keys('blablabla')

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'testFile.txt')           # добавляем к этому пути имя файла 
    element = browser.find_element(By.ID, 'file')
    element.send_keys(file_path)

    submit = browser.find_element(By.CSS_SELECTOR, '.btn')
    submit.click() 

finally:
    time.sleep(4)
    browser.close()
    browser.quit()    