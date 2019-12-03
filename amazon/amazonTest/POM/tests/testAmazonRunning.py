import unittest
from selenium import webdriver
from amazon.amazonTest.POM.pages.homepage import MainPage
from amazon.amazonTest.POM.pages.loginPage import LoginPage
from amazon.amazonTest.POM.pages.category import CategoryPage
from amazon.amazonTest.POM.pages.product import ProductPage


class AmazonTesting(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.amazon.com")
        self.driver.maximize_window()

    def test_Amazon(self):
        main_page = MainPage(self.driver)
        login_page = LoginPage(self.driver)
        category_page = CategoryPage(self.driver)
        product_page = ProductPage(self.driver)
        main_page.is_amazon()
        main_page.click_nav_sign_in()
        login_page.username_write()
        login_page.continue_click()
        login_page.password_write()
        login_page.sign_in()
        main_page.searching()
        main_page.searching_click()
        category_page.is_searching_page()
        category_page.pagination()
        category_page.is_pagination_two()
        category_page.two_pagination_three_product()
        product_page.add_to_list()
        product_page.wish_list()
        product_page.is_wish_list()
        product_page.view_list_show()
        product_page.is_wish_list_delete()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
