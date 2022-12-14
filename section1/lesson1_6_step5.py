# Поиск элемента по тексту в ссылке
# Section 1, module 6, step 5

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/find_link_text'

try:
    browser = webdriver.Chrome(executable_path='E:\My_files\Programming\PyProjects\StepikSeleniumCourse\drivers\chromedriver.exe')
    browser.get(link)
    # пауза що б побачити перехід на форму заповнення
    time.sleep(1)
    linkText = str(math.ceil(math.pow(math.pi, math.e)*10000))
    link = browser.find_element(By.LINK_TEXT, linkText)
    link.click()

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
    time.sleep(8)    
    browser.close()
    browser.quit()