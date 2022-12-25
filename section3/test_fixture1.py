from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"
# префиксы setup_*, teardown_* отвечают за порядок исполнения фикстур: до чего-то, после чего-то.
# постфиксы *_class, *_method и другие отвечают за уровень применения фикстур: ко всему классу, к каждому методу в классе и тд.

class TestMainPage1():
    # @classmethod декоратор, использованный для удобства чтения кода. 
    # Так мы дополнительно размечаем в коде, что метод ниже (в нашем примере с *_class) применяется ко всему классу.
    @classmethod
    def setup_class(self):
        # setup_class выполняется один раз перед запуском всех тестовых методов в классе
        print("\nstart browser for test suite..(один раз в класе)")
        self.browser = webdriver.Chrome(executable_path='E:\My_files\Programming\PyProjects\StepikSeleniumCourse\drivers\chromedriver.exe')

    @classmethod
    def teardown_class(self):
        # teardown_class выполянется один раз после
        print("\nquit browser for test suite..(один раз после выполнения")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


class TestMainPage2():

    def setup_method(self):
        # setup_method выполняется перед запуском каждого тестового метода в классе
        print("start browser for test..(каждий раз для каждого теста)")
        self.browser = webdriver.Chrome(executable_path='E:\My_files\Programming\PyProjects\StepikSeleniumCourse\drivers\chromedriver.exe')

    def teardown_method(self):
        # teardown_method выполняется каждый раз после
        print("quit browser for test..(каждий раз после каждого теста)")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

