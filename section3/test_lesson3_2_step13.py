from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class TestRegistrationForm(unittest.TestCase):
    def test_registration2(self):
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
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Registration failed!!")
        # assert "Congratulations! You have successfully registered!" == welcome_text
        
        browser.close()
        browser.quit()  

    def test_registration1(self):
        url = 'http://suninjuly.github.io/registration1.html'
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
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Registration failed!!")
        
        browser.close()
        browser.quit()          
           
        
if __name__ == "__main__":
    unittest.main()   


    