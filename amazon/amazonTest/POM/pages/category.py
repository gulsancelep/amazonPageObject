from amazon.amazonTest.POM.locators import MainPageLocators
from amazon.amazonTest.POM.actions.actionPage import Actions


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.Actions_Wait = Actions(driver)


class CategoryPage(BasePage):

    def is_searching_page(self):
        self.assertEqual(MainPageLocators.IS_SEARCHING_PAGE, self.driver.current_url)

    def pagination(self):
        self.Actions_Wait.click(MainPageLocators.PAGINATION, "XPATH")

    def is_pagination_two(self):
        actual = "17-32 of over 10,000 results for"
        self.assertEqual(self.Actions_Wait.is_checking(MainPageLocators.PAGINATION_TWO_TEXT), actual)

    def two_pagination_three_product(self):
        self.Actions_Wait.click(MainPageLocators.PRODUCT, "XPATH")