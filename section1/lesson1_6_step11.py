# Пир-ревью, У нас уже есть простой тест из предыдущего шага, который проверяет возможность зарегистрироваться на сайте.
# Однако обновленная страница доступна по другой ссылке. 
# Тест должен успешно проходить на странице http://suninjuly.github.io/registration1.html 
# но на http://suninjuly.github.io/registration2.html тест должен падть с ошибкой NoSuchElementException. 
# Section 1, module 6, step 11



from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    url = 'http://suninjuly.github.io/registration2.html'
    browser = webdriver.Chrome(executable_path='E:\My_files\Programming\PyProjects\StepikSeleniumCourse\drivers\chromedriver.exe')
    browser.get(url=url)

    reqFirstNameField = browser.find_element(By.CSS_SELECTOR, '.form-control.first:required')
    reqFirstNameField.send_keys('Name')
    reqMailField = browser.find_element(By.CSS_SELECTOR, '.form-control.third:required')
    reqMailField.send_keys('kek@mail')
    phoneField = browser.find_element(By.CSS_SELECTOR, '.form-control.first[placeholder="Input your phone"]')
    phoneField.send_keys('8800555')
    addressField = browser.find_element(By.CSS_SELECTOR, '.form-control.second')
    addressField.send_keys('Jump street 21')

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
   
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(4)
    browser.close()
    browser.quit()



